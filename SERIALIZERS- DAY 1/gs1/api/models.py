from django.db import models

# Create your models here.

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     roll = models.IntegerField()
#     city = models.CharField(max_length=100)
    
    
    
    
# class Quote(models.Model):
#     text = models.TextField(max_length=100)
#     author = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
    
    
#     def __str__(self):
#         return f"{self.text[:50]} - {self.author}"

# quotes/models.py

from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]} - {self.author}"
