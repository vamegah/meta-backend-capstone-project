from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
        read_only = ['id']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']

class GroupNameField(serializers.RelatedField):
    def to_representation(self, value):
        # Return the group name
        return value.name

class UserSerializer(serializers.ModelSerializer):
    groups = GroupNameField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

