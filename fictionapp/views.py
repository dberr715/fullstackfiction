from django.shortcuts import render
from rest_framework import viewsets
from .models import BookList

# Create your views here.

from .serializers import BooklistSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookList.objects.all().order_by("title")
    serializer_class = BooklistSerializer


def index(request):
    all_books = BookList.objects.all()
    context = {"all_books": all_books}
    return render(request, "index.html", context)
