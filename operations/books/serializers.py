from rest_framework import serializers
from operations.models import Author,Book,Category

class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self,value):
        return value

class BookSerializer(serializers.ModelSerializer):
    
    # author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    author = serializers.SlugRelatedField(queryset=Author.objects.all(), many=True,slug_field="name")
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), many=True,slug_field="name")
    class Meta:
        model = Book
        fields =('__all__')

    # def get_author(self,obj):
    #     author = AuthorSerializer(obj.author.all(),many=True).data
    #     return author
    # def get_category(self,obj):
    #     category = CategorySerializer(obj.category.all(),many=True).data
    #     return category

class AuthorSerializer(serializers.ModelSerializer):
    author = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    category = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('__all__')
    