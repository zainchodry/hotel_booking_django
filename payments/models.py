from django.db import models
from django.contrib.auth.models import User
from hotel.models import Booking

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash at Hotel'),
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Booking {self.booking.id} by {self.user.username}"
