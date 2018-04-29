from rest_framework import serializers
from . import models



class GameSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('colorCode',)
        model = models.Game

    def create(self, validated_data):
        print ('validated_data')
        print (validated_data)
        return Game.objects.create(**validated_data)

class GameCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Game
		fields = ['idGame',
			'colorCode',
		]