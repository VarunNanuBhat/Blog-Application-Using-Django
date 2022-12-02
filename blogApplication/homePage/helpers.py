from django.utils.text import slugify
from django.conf import settings
from django.core.mail import send_mail
import random
import string



def generate_random_string(length_of_string):
    result = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length_of_string))
    return result


def generate_slug(text):
    from .models import BlogModel
    new_slug = slugify(text)
    if BlogModel.objects.filter(slug = new_slug).exists():       # checking if the slug created is already present or not.
        return generate_slug(text + generate_random_string(5))         # if found true, add 5 random chars to the slug to make it unique
    return new_slug

def send_mail_to_user(token, email):
    subject = f"Your account needs to be verified"
    message = f"Hi, Please paste the link to verify your account http://127.0.0.1:8000/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
