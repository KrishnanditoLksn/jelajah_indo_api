from rest_framework import serializers

from plesirbe.models.destination import Destination


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = "__all__"