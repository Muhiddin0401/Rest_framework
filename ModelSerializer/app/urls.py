from django.urls import path
from .views import movie_api, movie_detail, actor_api, actor_detail

urlpatterns = [
    # movie get, pot
    path('', movie_api),
    # movie get, put, patch
    path('movie_detail/<slug:slug>/',movie_detail),
    # actor get, pot
    path('actor_api/', actor_api),
    # actor get, put, patch
    path('actor_detail/<slug:slug>/', actor_detail),
]