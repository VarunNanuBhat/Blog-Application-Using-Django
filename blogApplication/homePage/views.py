from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def add_blog(request):
    return render(request, 'add_blog.html')

def register_view(request):
    return render(request, 'register.html')
