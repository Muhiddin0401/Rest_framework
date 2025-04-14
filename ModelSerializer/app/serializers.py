from rest_framework import serializers
from .models import Movie, Actors


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ActorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = "__all__"