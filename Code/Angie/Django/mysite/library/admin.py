from django.contrib import admin
from .models import Author
from .models import Book
# from .models import CheckSystem

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
# admin.site.register(CheckSystem)