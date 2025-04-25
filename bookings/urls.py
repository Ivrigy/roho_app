from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_service, name='book_service'),
    path('my-bookings/', views.my_bookings, name='my_bookings'), 
]
