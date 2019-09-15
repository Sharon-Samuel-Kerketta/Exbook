from rest_framework import serializers
from operations.models import Author,Book,Category

class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self,value):
        return value

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields =('__all__')

    def get_author(self,obj):
        author = AuthorSerializer(obj.author.all(),many=True).data
        return author
    def get_category(self,obj):
        category = CategorySerializer(obj.category.all(),many=True).data
        return category
    