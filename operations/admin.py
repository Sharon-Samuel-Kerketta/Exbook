from django.contrib import admin

# Register your models here.

from .models import Book,Author,Category,User

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(User)