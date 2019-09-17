from rest_framework import viewsets
from operations.books.serializers import BookSerializer,AuthorOnlySerializer, CategoryOnlySerializer
from operations.models import Book,Author,Category

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorOnlySerializer
    queryset = Author.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryOnlySerializer
    queryset = Category.objects.all()

