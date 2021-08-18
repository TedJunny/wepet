from django.urls import path
from movies import views

urlpatterns = [
    path("/movies", views.MovieListView.as_view()),
    path("/actors", views.ActorListView.as_view()),
    path("/movies_actors", views.MovieActorListView.as_view()),
]
