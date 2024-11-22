# from rest_framework import viewsets, status
# from rest_framework import serializers
# from rest_framework.response import Response
# from levelupapi.models import GameType


# class GameTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GameType
#         fields = ["id", "label"]


# class GameTypeViewSet(viewsets.ViewSet):
#     def list(self, request):
#         gametypes = GameType.objects.all()
#         serializer = GameTypeSerializer(gametypes, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         try:
#             gametype = GameType.objects.get(pk=pk)
#             serializer = GameTypeSerializer(gametype)
#             return Response(serializer.data)
#         except GameType.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import GameType


class GameTypeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        game_type = GameType.objects.get(pk=pk)
        serializer = GameTypeSerializer(game_type)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        game_types = GameType.objects.all()
        serializer = GameTypeSerializer(game_types, many=True)
        return Response(serializer.data)
    
class GameTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types"""
    class Meta:
        model = GameType
        fields = ('id', 'label')        