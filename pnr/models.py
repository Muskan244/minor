'''from django.db import models

# Create your models here.
class PNR(models.Model):
    pnr_number = models.CharField(max_length=10, unique=True)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pnr_number} - Valid: {self.is_valid}"'''

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.db import models
from django.utils import timezone

# Station model to store train stations
class Station(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.name}"

# Parcel model to track details of each parcel
class Parcel(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_parcels')
    traveling_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='travel_parcels')
    description = models.TextField()
    weight = models.FloatField()
    origin = models.CharField(max_length=255, default="Unknown")
    destination = models.CharField(max_length=255)
    deadline = models.DateField()
    status = models.CharField(max_length=10, default='pending')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    confirmed = models.BooleanField(default=False)  # Track if sender has confirmed the traveler

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def confirm_traveler(self):
        self.confirmed = True
        self.save()

    def __str__(self):
        return self.description

# TravelDetails model to store details of a traveler's journey
class TravelDetails(models.Model):
    traveler = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='travel_origin')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='travel_destination')
    travel_date = models.DateField()

    def __str__(self):
        return f"{self.origin} to {self.destination} on {self.travel_date}"

# Message model for parcel-related communication
class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_date = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient} about Parcel {self.parcel}"

# Notification model to manage user notifications
class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

# PNR model to track train PNR details
class PNR(models.Model):
    pnr_number = models.CharField(max_length=10, unique=True)
    is_valid = models.BooleanField(default=False)
    travel_details = models.OneToOneField(TravelDetails, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.pnr_number} - Valid: {self.is_valid}"
