from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie, Actors
from .serializers import MovieSerializers, ActorsSerializers

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
    except Exception as e:
        response = {"error": e}
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
        response = {"success": True}
    except Exception as e:
        response = {"error": e}
        return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
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

@api_view(["POST"])
def tabrik_api(request):
    ism = request.data["ism"]
    familiya = request.data["familiya"]
    age = request.data["age"]
    return Response(data={"Tabrik": f"Assalomu aleykum {ism} {familiya}. Sizni {age} yoshingiz bilan tabriklaymiz"})