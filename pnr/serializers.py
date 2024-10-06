from rest_framework import serializers
from .models import PNR, Parcel, TravelDetails, Message, Notification

class PNRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PNR
        fields = ["pnr_number", "is_valid"]

    '''def validate_pnr_number(self, value):
        if not value.startswith('1'):
            raise serializers.ValidationError("PNR must start with '1'")
        elif len(value) != 10:
            raise serializers.ValidationError("PNR must have 10 characters")
        return value
'''

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ['id', 'description', 'weight', 'origin', 'destination', 'deadline', 'sender', 'traveling_user']

class TravelDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelDetails
        fields = ['id', 'origin', 'destination', 'travel_date', 'traveler']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'parcel', 'subject', 'message', 'sent_date']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'read']