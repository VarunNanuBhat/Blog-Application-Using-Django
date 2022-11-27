from django.template.defaulttags import url
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', homePage, name='homePage'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('add-blog/', add_blog, name='add_blog'),
]