from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits= 6, decimal_places = 2)
    published_date = models.DateField()
    in_stock = models.BooleanField(default = True)
    
    def __str__(self):
        return self.title
    