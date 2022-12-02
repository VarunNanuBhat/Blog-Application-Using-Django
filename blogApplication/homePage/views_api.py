from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from .helpers import generate_random_string, send_mail_to_user


class LoginView(APIView):
    '''
    if something unexpected error occurs
    '''
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = "Something went wrong"
        try:
            data = request.data
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            if data.get('password') is None:
                response['message'] = 'Key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user is None:
                response['message'] = 'Invalid username, user not found'
                raise Exception('Invalid username, user not found')

            user_obj = authenticate(username=data.get('username'), password=data.get('password'))

            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'Invalid password'
                raise Exception('Invalid password')

        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()


class RegisterView(APIView):
    '''
    if something unexpected error occurs
    '''
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = "Something went wrong"
        try:
            data = request.data
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            if data.get('password') is None:
                response['message'] = 'Key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user:
                response['message'] = 'User name already taken'
                raise Exception('user name already taken')

            if not Profile.objects.filter(user=check_user).first().is_verified:
                response['message'] = "Your profile is not yet verified"
                raise Exception("Profile not yet verified")

            user_obj = User.objects.create(email=data.get('username'), username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()

            token = generate_random_string(20)
            Profile.objects.create(user=user_obj, token=token)
            send_mail_to_user(token, data.get('username'))
            response['status'] = 200
            response['message'] = 'User created'

        except Exception as e:
            print(e)

        return Response(response)

RegisterView = RegisterView.as_view()

