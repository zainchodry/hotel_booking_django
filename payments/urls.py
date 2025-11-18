from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('pay/<int:booking_id>/', views.make_payment, name='make_payment'),
    path('success/<int:booking_id>/', views.payment_success, name='payment_success'),
]
