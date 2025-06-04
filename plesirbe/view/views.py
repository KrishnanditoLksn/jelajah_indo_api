from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from plesirbe.models.destination import Destination
from plesirbe.pagination.small_result_pagination import SmallResultsSetPagination
from plesirbe.recommender.destination_recommender import get_similar_destinations
from plesirbe.serializer import DestinationSerializer
from rest_framework.pagination import LimitOffsetPagination

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


@api_view(['GET'])
def paginated_destination_list(request):
    queryset = Destination.objects.all()
    paginator = LimitOffsetPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    serializer = DestinationSerializer(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def destination_detail(self, ids):
    try:
        destination = Destination.objects.get(id=ids)
        serializer = DestinationSerializer(destination)
        sim_dest = get_similar_destinations(ids, 5)
        sim_destinations_serializer = DestinationSerializer(sim_dest, many=True)

        """Return JSON Response that consist detail destination """
        return Response({
            'destination': serializer.data,
            'recommendations': sim_destinations_serializer.data
        })

    except Destination.DoesNotExist:
        return Response({
            'Message': "Item Not Found !!!"
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def search_destination(request):
    query = request.query_params.get('query', None)

    if not query:
        return Response(
            {'message': 'Query parameter is required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    destinations = Destination.objects.filter(place_name__icontains=query)

    if not destinations.exists():
        return Response(
            {'message': 'Item not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = DestinationSerializer(destinations, many=True)
    return Response({
        'Destination': serializer.data
    }, status=status.HTTP_200_OK)
