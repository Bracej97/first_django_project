from django.contrib import admin
from .models import Author
from .models import Book  # Replace with your model name

admin.site.register(Author)
admin.site.register(Book)
