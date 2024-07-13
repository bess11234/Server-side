from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=150) # null=False by default
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    
    def __str__(self):
        return "%s %s"%(self.first_name, self.last_name)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField(default=0)
    created_by = models.ForeignKey(Author, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField("blogs.Category") # เป็นการสร้างอีก Table ให้ลองรับ M-M โดยถ้าตามที่กำหนดนี้ Table จะชื่อ blog_categories
    
    def __str__(self):
        return "%s (%s)"%(self.title, self.like)

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# class Blog_category(models.Model):
#     category_id = models.ForeignKey(Category, on_delete=models.CASCADE, primary_key=True)
#     blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, primary_key=True)
#     models.ManyToManyField()