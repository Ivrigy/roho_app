from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking


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


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user,
    )
    return render(
        request,
        'bookings/my_bookings.html',
        {'bookings': bookings},
    )


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
    )

    if request.method == 'POST':
        booking.delete()
        return redirect(
            'my_bookings',
        )

    return render(
        request,
        'bookings/confirm_delete.html',
        {'booking': booking},
    )


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
    )

    if request.method == 'POST':
        form = BookingForm(
            request.POST,
            instance=booking,
        )
        if form.is_valid():
            form.save()
            return redirect(
                'my_bookings',
            )
    else:
        form = BookingForm(
            instance=booking,
        )

    return render(
        request,
        'bookings/edit_booking.html',
        {
            'form': form,
            'booking': booking,
        },
    )
