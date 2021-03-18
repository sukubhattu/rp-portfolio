from django.contrib import admin

# Import models
from .models import Book

# Register your models here.
admin.site.register(Book)