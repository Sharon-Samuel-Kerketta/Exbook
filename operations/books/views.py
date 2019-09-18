from rest_framework import viewsets
from operations.books.serializers import BookSerializer,AuthorOnlySerializer, CategoryOnlySerializer
from operations.models import Book,Author,Category

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

# def get_queryset(self):
#         queryset= Author.objects.all()
#         print(queryset)
#         data = list(Author.objects.all())
#         authors={}
#         list_of_authors=[]
#         for author in data :
#             list_of_authors.append(author.name)
#         authors['Author']=list_of_authors
#         print(authors)
#         return Author.objects.values("author",list_of_authors)
        

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorOnlySerializer
    queryset = Author.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryOnlySerializer
    queryset = Category.objects.all()

