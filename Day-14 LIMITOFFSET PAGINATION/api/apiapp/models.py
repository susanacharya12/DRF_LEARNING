from django.db import models

# Create your models here.

class Hostel(models.Model):
    ROOM_TYPES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),
    ]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    
    class Meta:
        unique_together = ('name', 'room_type')  # Prevent duplicate hostel-room type entries

    def __str__(self):
        return f"{self.name} - {self.get_room_type_display()} ({self.fee})"