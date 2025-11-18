from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from hotel.models import Booking
from .models import Payment
from .forms import PaymentForm

@login_required
def make_payment(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    
    if hasattr(booking, 'payment') and booking.payment.is_paid:
        return render(request, 'payments/payment_success.html', {'booking': booking})

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.user = request.user
            payment.amount = booking.room.price_per_night
            payment.is_paid = True
            payment.save()
            booking.room.is_available = False
            booking.room.save()
            return redirect('payments:payment_success', booking_id=booking.id)
    else:
        form = PaymentForm()

    return render(request, 'payments/make_payment.html', {'form': form, 'booking': booking})

@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    return render(request, 'payments/payment_success.html', {'booking': booking})
