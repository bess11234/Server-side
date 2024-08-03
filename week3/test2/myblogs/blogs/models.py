from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    like = models.IntegerField()
    created_by = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    
