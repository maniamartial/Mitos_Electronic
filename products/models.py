from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Electronic(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=500)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
