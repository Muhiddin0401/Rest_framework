from django.urls import path
from .views import *

urlpatterns = [
    # movie get, pot
    path('', movie_api),
    path('', tabrik_api),
    # movie get, put, patch
    path('movie_detail/<slug:slug>/',movie_detail),
    # actor get, pot
    path('actor_api/', actor_api),
    # actor get, put, patch
    path('actor_detail/<slug:slug>/', actor_detail),
]