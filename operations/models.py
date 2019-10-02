from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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

class Author(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Author'

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category'

class Book(models.Model) :
    isbn = models.CharField(max_length=13,null=True,blank=True,unique=True)
    name = models.CharField(max_length=255)
    author = models.ManyToManyField(Author,related_name="author")
    category = models.ManyToManyField(Category, related_name="category")
    publisher = models.CharField(max_length=255,null=True)
    description = models.TextField()
    condition = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    original_price = models.IntegerField()
    discounted_price = models.IntegerField()
    language = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user")
    user_fire_id = models.CharField(max_length=100)
    image = models.ImageField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Book'







