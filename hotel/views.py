from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Hotel, Room
from .forms import BookingForm

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    rooms = hotel.rooms.all()  # all rooms of this hotel
    return render(request, 'room_detail.html', {'hotel': hotel, 'rooms': rooms})


@login_required
def book_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if not room.is_available:
        return render(request, 'room_unavailable.html', {'room': room})

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            booking.save()
            room.is_available = False
            room.save()
            return redirect('hotel:hotel_list')
    else:
        form = BookingForm()

    return render(request, 'book_room.html', {'form': form, 'room': room})
