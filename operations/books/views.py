from rest_framework import viewsets
from operations.books.serializers import BookSerializer
from operations.models import Book,Author,Category

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
