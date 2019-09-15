from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=10,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "User"

    def __str__(self):
        return self.username


class Book(models.Model) :
    isbn = models.CharField(max_length=13,null=True,blank=True)
    name = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255,null=True)
    condition = models.IntegerField()
    language = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Book'

class Author(models.Model):
    name = models.CharField(max_length=120)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="author")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Author'

class Category(models.Model):
    name = models.CharField(max_length=20)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="category")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category'






