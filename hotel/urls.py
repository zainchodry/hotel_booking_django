from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('room/<int:pk>/book/', views.book_room, name='book_room'),
]
