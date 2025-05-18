from rest_framework.decorators import api_view
from rest_framework.response import Response

from plesirbe.models import Destination
from plesirbe.serializer import DestinationSerializer


@api_view(['GET'])
def plesir_base_url(self):
    return Response({
        "message": "Plesir Travel Recommendation System REST API "
    })


@api_view(['GET'])
def list_of_destinations(self):
    destination = Destination.objects.all()
    serializer = DestinationSerializer(destination, many=True)
    """Return JSON Response that consist list of destination """
    return Response({
        'destination': serializer.data
    })
