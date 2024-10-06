import requests
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import PNR, Parcel, TravelDetails, Message, Notification
from .serializers import PNRSerializer, ParcelSerializer, TravelDetailsSerializer, MessageSerializer, NotificationSerializer
from .services import check_pnr_status

# Create your views here.
class PNRList(generics.ListCreateAPIView):
    queryset = PNR.objects.all()
    serializer_class = PNRSerializer

    def post(self, request, *args, **kwargs):
        pnr_number = request.data.get('pnr_number')
        # check if the PNR already exists in the database
        pnr_instance = PNR.objects.filter(pnr_number=pnr_number).first()

        if pnr_instance:
            # Return the stored result if PNR already exists
            return Response({
                "pnr_number": pnr_instance.pnr_number,
                "is_valid": pnr_instance.is_valid,
                "message": "PNR already checked."
            }, status=status.HTTP_200_OK)

        # Validate the PNR 
        valid = check_pnr_status(pnr_number)
        if valid == None:
            is_valid = False
        else:
            is_valid = True
        
        # Create a new PNR entry with the validation result
        new_pnr = PNR.objects.create(pnr_number=pnr_number, is_valid=is_valid)

        return Response({
            "pnr_number": new_pnr.pnr_number,
            "is_valid": new_pnr.is_valid,
            "message": "PNR checked and result saved."
        }, status=status.HTTP_201_CREATED)


class PNRDelete(generics.RetrieveDestroyAPIView):
    queryset = PNR.objects.all()
    serializer_class = PNRSerializer
    lookup_field = 'pnr_number'

    def delete(self, request, *args, **kwargs):
        # Retrieve and delete the PNR object
        pnr_instance = self.get_object()
        self.perform_destroy(pnr_instance)
        return Response({
            "message": f"PNR {pnr_instance.pnr_number} deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)
    
