from django.test import TestCase
from django.urls import reverse
from restaurant.views import BookingView
from restaurant.forms import BookingForm
from restaurant.models import Booking
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import BookingSerializer


class BookingViewTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

        self.booking1 = Booking.objects.create(
            name = 'John Doe',
            number_of_guests = 2,
            booking_date = timezone.now()
        )
        self.booking2 = Booking.objects.create(
            name = 'Jane Smith',
            number_of_guests = 4,
            booking_date = timezone.now()
        )
        self.valid_payload = {
            'name': 'Test Booking',
            'number_of_guests': 3,
            'booking_date': timezone.now()
        }
        self.invalid_payload = {
            'name': '',
            'number_of_guests': '',
            'booking_date': ''
        }

    def test_get_all_bookings(self):
        response = self.client.get(reverse('bookings'))
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_booking(self):
        response = self.client.post(
            reverse('bookings'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_booking_invalid_data(self):
        response = self.client.post(
            reverse('bookings'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_data_from_form(self):
        form = BookingForm(data=self.valid_payload)
        self.assertTrue(form.is_valid())
        data = BookingView().get_data_from_form(form)
        self.assertEqual(data, self.valid_payload)

    def test_retrieve_valid_single_booking(self):
        response = self.client.get(
            reverse('booking-detail', kwargs={'pk': self.booking1.id})
        )
        booking = Booking.objects.get(id=self.booking1.id)
        serializer = BookingSerializer(booking)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

