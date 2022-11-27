from django.template.defaulttags import url
from django.urls import include, path
from .views_api import *

urlpatterns = [
    path('login/', LoginView),
    path('register/', RegisterView)
]