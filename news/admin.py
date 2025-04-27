from django.contrib import admin

from news.models import Author, Book

admin.site.register(Author)
admin.site.register(Book)