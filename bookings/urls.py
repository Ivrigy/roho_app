from django.urls import path
from . import views
from django.http import HttpResponse


def my_bookings(request):
    return HttpResponse("Coming soon...")


urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_service, name='book_service'),
    path('my-bookings/', my_bookings, name='my_bookings'),
]
