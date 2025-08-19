from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    grade = models.CharField(max_length=5)

    def __str__(self):
        return self.name


   