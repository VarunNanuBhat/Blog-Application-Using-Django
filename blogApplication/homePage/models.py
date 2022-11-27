from django.db import models
from django.contrib.auth.models import User     #for creating user table
from froala_editor.fields import FroalaField
from .helpers import *

# Create your models here.

'''
creating tables and fields
'''

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add will add timestamp only at the time of creation.
    upload_at = models.DateTimeField(auto_now=True)         # new timestamp will be created whenever there is an update.

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)