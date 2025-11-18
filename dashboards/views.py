from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hotel.models import Booking

@login_required
def dashboard_view(request):
    user = request.user
    user_bookings = Booking.objects.filter(user=user).order_by('-created_at')[:5]

    context = {
        'user': user,
        'bookings': user_bookings,
    }
    return render(request, 'index.html', context)
