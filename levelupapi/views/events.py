from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from levelupapi.models import Gamer, Event, Game
from levelupapi.views import GameSerializer
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet

class EventSerializer(serializers.ModelSerializer):
    """Serializer for Event objects"""

    game = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all(), source='gameId'
    )
    organizer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='organizerId'
    )

    class Meta:
        model = Event
        fields = (
            'id',
            'description',
            'title',
            'date',
            'time',
            'game',
            'organizer'
        )
        depth = 1

        
        
class EventView(ViewSet):
    """View for handling Event requests"""

    def list(self, request):
        """Handle GET requests to retrieve all events"""
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single event"""
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response(
                {"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """Handle POST requests to create a new event"""
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Handle PUT requests to update an event"""
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(None, status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Event.DoesNotExist:
            return Response(
                {"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        """Handle DELETE requests to delete an event"""
        try:
            event = Event.objects.get(pk=pk)
            event.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response(
                {"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND
            )