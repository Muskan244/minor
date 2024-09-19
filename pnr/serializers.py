from rest_framework import serializers
from .models import PNR

class PNRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PNR
        fields = ["pnr_number", "is_valid"]