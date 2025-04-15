from rest_framework import serializers
from .models import Movie, Actors


class ActorsSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    slug = serializers.SlugField(required=False, allow_blank=True)
    birth_date = serializers.DateField()

    def validate(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Ism kamida 2 ta belgidan iborat boʻlishi kerak.")
        return value

    def create(self, validated_date):
        return Actors.objects.create(**validated_date)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.birth_data = validated_data.get('birth_date', instance.birth_data)
        instance.save()
        return instance

class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=150)
    slug = serializers.SlugField(required=False, allow_blank=True)
    year = serializers.IntegerField(default=1920)
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actors.objects.all(),
        many=True
    )
    genre = serializers.CharField(max_length=1000)

    def validate(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Kino nomi kamida 3 ta belgidan iborat boʻlishi kerak.")
        return value

    def create(self, validated_date):
        # actorlarni olish
        actors_data = validated_date.pop('actors',[])
        # Movini olish
        movie = Movie.objects.create(**validated_date)
        # actor qo'shish
        movie.actors.set(actors_data)

        return movie


    def update(self, instance, validated_data):
        # actorsni alohida olish
        actors_data = validated_data.pop('actors', None)
        # qolgan ma'lumotlarni yangilash
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.year = validated_data.get('year', instance.year)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()

        if actors_data is not None:
            instance.actors.set(actors_data)
        return instance


# class MovieSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = "__all__"
#
# class ActorsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Actors
#         fields = "__all__"