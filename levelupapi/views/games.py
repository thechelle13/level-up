from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from levelupapi.models import Gamer, Game, GameType
from levelupapi.views import GameTypeSerializer

from rest_framework.viewsets import ViewSet

class GameSerializer(serializers.ModelSerializer):
    gametype = GameTypeSerializer()

    class Meta:
        model = Game
        fields = ('id', 'title', 'maker', 'skill_level', 'number_of_players', 'gametype', 'gamer')
        depth = 1

class GameView(ViewSet):

    def create(self, request):
        """Handle POST operations for creating a game"""
        gamer = Gamer.objects.get(user=request.auth.user)
        gametype = GameType.objects.get(pk=request.data['gameTypeId'])

        game = Game.objects.create(
            title=request.data['title'],
            maker=request.data['maker'],
            skill_level=request.data['skillLevel'],
            number_of_players=request.data['numberOfPlayers'],
            gametype=gametype,
            gamer=gamer
        )
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single game"""
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist:
            return Response({'message': 'Game not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Handle PUT requests for a game"""
        game = Game.objects.get(pk=pk)
        gametype = GameType.objects.get(pk=request.data['gameTypeId'])

        game.title = request.data['title']
        game.maker = request.data['maker']
        game.skill_level = request.data['skillLevel']
        game.number_of_players = request.data['numberOfPlayers']
        game.gametype = gametype
        game.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a game"""
        try:
            game = Game.objects.get(pk=pk)
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Game.DoesNotExist:
            return Response({'message': 'Game not found'}, status=status.HTTP_404_NOT_FOUND)
