import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=25)
    

    def __str__(self):
        return self.name
    

class ISBN(models.Model):
    isbn_number       = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  #uuid field search
    author_name       = models.CharField(max_length=25)
    book_title        = models.CharField(max_length=40)

    def __str__(self):
        return str(self.isbn_number)

class Book(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="books")
    tag         = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True, related_name="tag")
    categories  = models.ManyToManyField(Category)
    isbn        = models.OneToOneField(ISBN, on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.title
