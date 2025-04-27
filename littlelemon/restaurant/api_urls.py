# restaurant/api_urls.py
from django.urls import path
from . import views

app_name = 'restaurant'
urlpatterns = [
    path('bookings/', views.bookings, name='bookings'),
    path('menu/', views.menu, name='menu'),
]
 