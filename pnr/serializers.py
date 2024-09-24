from rest_framework import serializers
from .models import PNR

class PNRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PNR
        fields = ["pnr_number", "is_valid"]

    def validate_pnr_number(self, value):
        if not value.startswith('1'):
            raise serializers.ValidationError("PNR must start with '1'")
        elif len(value) != 10:
            raise serializers.ValidationError("PNR must have 10 characters")
        return value
