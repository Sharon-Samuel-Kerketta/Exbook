from operations.books.serializers import BookSerializer,AuthorSerializer,CategoryOnlySerializer
from rest_framework.routers import DefaultRouter
from operations.books.views import BookViewSet,AuthorViewSet,CategoryViewSet
from django.urls import reverse

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'authors',AuthorViewSet,base_name='authors')
router.register(r'categories',CategoryViewSet,base_name='categories')
urlpatterns = router.urls
