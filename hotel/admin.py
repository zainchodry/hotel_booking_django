from django.contrib import admin
from .models import Hotel, Room, Booking

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'hotel', 'room_type', 'price_per_night', 'is_available')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'check_in', 'check_out', 'created_at')
