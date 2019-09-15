from operations.books.serializers import BookSerializer 
from rest_framework.routers import DefaultRouter
from operations.books.views import BookViewSet
from django.urls import reverse

router = DefaultRouter()
router.register(r'', BookViewSet, basename='books')
urlpatterns = router.urls
