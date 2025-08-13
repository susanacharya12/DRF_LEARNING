from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    starttime = models.TimeField()
    endtime = models.TimeField()
    
    def __str__(self):
        return self.name
    