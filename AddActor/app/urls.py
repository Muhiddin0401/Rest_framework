from django.urls import path
from .views import movie_api, movie_detail, actor_api, actor_detail, AddActorToMovieView

urlpatterns = [
    # movie get, pot
    path('', movie_api),
    # movie get, put, patch
    path('movie_detail/<slug:slug>/',movie_detail),
    # actor get, pot
    path('actor_api/', actor_api),
    # actor get, put, patch
    path('actor_detail/<slug:slug>/', actor_detail),
    # Add Actor to Movie
    path('api/movies/<slug:slug>/add_actor/', AddActorToMovieView.as_view(), name = "add_actor_to_movie")
]