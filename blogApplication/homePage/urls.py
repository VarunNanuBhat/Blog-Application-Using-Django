from django.template.defaulttags import url
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', homePage, name='homePage'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('add-blog/', add_blog, name='add_blog'),
    path('blog-detail/<slug>', blog_detail, name='blog_detail'),
    path('see-blog/', see_blog, name='see_blog'),
    path('blog-delete/<id>', blog_delete, name='blog_delete'),
    path('update-blog/<slug>/', blog_update, name='blog_update'),
]