from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Tags(models.Model):
    tag_name=models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

class Products(models.Model):
    product_name=models.CharField(max_length=200)
    tags=models.ManyToManyField(Tags)
    image=models.ImageField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField()

    def __str__(self):
        return self.product_name
