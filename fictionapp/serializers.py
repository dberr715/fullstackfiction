from .models import BookList
from rest_framework import serializers


class BooklistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookList
        fields = ["title", "author", "description"]
