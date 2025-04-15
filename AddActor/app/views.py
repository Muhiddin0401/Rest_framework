from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import Movie, Actors
from .serializers import MovieSerializers, ActorsSerializers


class AddActorToMovieView(CreateAPIView):
    serializer_class = ActorsSerializers

    def post(self, request, slug, *args, **kwargs):
        try:
            movie = Movie.objects.get(slug=slug)
        except ObjectDoesNotExist:
            return Response(
                data = {"error": "Bunday film topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        actor = serializer.save()

        movie.actors.add(actor)
        return Response(
            data={
                "message": f"Actor {actor.name} successfully added to movie {movie.title}",
                "actor": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

@api_view(["GET", "POST"])
def actor_api(request):
    if request.method=="GET":
        actors = Actors.objects.all()
        serializer = ActorsSerializers(actors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method=="POST":
        serializer = ActorsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def actor_detail(request, slug):
    try:
        actor = Actors.objects.get(slug=slug)
        response = {"success": True}
    except:
        response = {"error": "Bunday malumot yo`q"}
        return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
    if request.method=="GET":
        serializer = ActorsSerializers(actor)
        response["data"] = serializer.data
        return Response(data=response, status=status.HTTP_200_OK)
    elif request.method=="PUT":
        serializer = ActorsSerializers(actor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PATCH":
        serializer = ActorsSerializers(actor, data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            return Response(data=response, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        actor.delete()
        response["message"] = "Actor deleted successfully"
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def movie_api(request):
    if request.method=="GET":
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method=="POST":
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def movie_detail(request, slug):
    try:
        movie = Movie.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return Response(
            data={"error": "Bunday ma'lumot yo‘q"},
            status=status.HTTP_417_EXPECTATION_FAILED
        )
    except Exception as e:
        return Response(
            data={"error": str(e)},
            status=status.HTTP_417_EXPECTATION_FAILED
        )

    response = {"success": True}

    if request.method=="GET":
        serializer = MovieSerializers(movie)
        response["data"] = serializer.data
        return Response(data=response, status=status.HTTP_200_OK)
    elif request.method=="PUT":
        serializer = MovieSerializers(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            return Response(data=response, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PATCH":
        serializer = MovieSerializers(movie, data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        movie.delete()
        response["message"] = "Movie deleted successfully"
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)