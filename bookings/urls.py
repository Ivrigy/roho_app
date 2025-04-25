from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_service, name='book_service'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('edit-booking/<int:booking_id>/',
         views.edit_booking, name='edit_booking'),
    path('delete-booking/<int:booking_id>/',
         views.delete_booking, name='delete_booking'),
]
