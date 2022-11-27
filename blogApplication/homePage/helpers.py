from django.utils.text import slugify
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

