from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.hotel.name})"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.room}"
