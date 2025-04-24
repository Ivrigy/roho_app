from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm


def home(request):
    return render(request, 'home.html')


@login_required
def book_service(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings/book_service.html', {'form': form})
