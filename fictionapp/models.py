from django.db import models


# Create your models here.
class BookList(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField()

    def __str__(self):
        return self.title
