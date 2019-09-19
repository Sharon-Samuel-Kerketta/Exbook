from rest_framework import viewsets
from operations.books.serializers import BookSerializer,AuthorOnlySerializer, CategoryOnlySerializer
from operations.models import Book,Author,Category
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorOnlySerializer
    queryset = Author.objects.all()
    def list(self,request):
        data = list(Author.objects.all())
        authors={}
        list_of_authors=[]
        for author in data :
            list_of_authors.append(author.name)
        return Response({"authors" : list_of_authors})
        

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryOnlySerializer
    queryset = Category.objects.all()
    def list(self,request):
        data = list(Category.objects.all())
        categories={}
        list_of_categories=[]
        for category in data :
            list_of_categories.append(category.name)
        return Response({"categories" : list_of_categories})

