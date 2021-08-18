import json

from django.http import JsonResponse
from django.views import View

from movies.models import Actor, Movie


class MovieListView(View):
    def post(self, request):
        data = json.loads(request.body)
        movie = Movie.objects.create(
            title=data["title"],
            release_date=data["release_date"],
            running_time=data["running_time"],
        )

        return JsonResponse({"MESSAGE": "CREATED"}, status=201)

    def get(self, request):
        result = []
        movies = Movie.objects.all()

        for movie in movies:
            actors = movie.actors.all()
            result.append(
                {
                    "title": movie.title,
                    "release_date": movie.release_date,
                    "running_time": movie.running_time,
                    "actors": list(actors.values()),
                }
            )
        return JsonResponse({"results": result}, status=200)


class ActorListView(View):
    def post(self, request):
        data = json.loads(request.body)
        actor = Actor.objects.create(
            first_name=data["first_name"],
            last_name=data["last_name"],
            date_of_birth=data["date_of_birth"],
        )
        movie = Movie.objects.get(id=data["movies_id"])

        actor.movies.add(movie)
        return JsonResponse({"MESSAGE": "CREATED"}, status=201)

    def get(self, request):
        result = []
        actors = Actor.objects.all()

        for actor in actors:
            movies = actor.movies.all()
            result.append(
                {
                    "first_name": actor.first_name,
                    "last_name": actor.last_name,
                    "date_of_birth": actor.date_of_birth,
                    "movies": list(movies.values()),
                }
            )

        return JsonResponse({"results": result}, status=200)


class MovieActorListView(View):
    def post(self, request):
        data = json.loads(request.body)
        movie = Movie.objects.get(title=data["movie_title"])
        actor = Actor.objects.get(first_name=data["actor_first_name"])

        movie.actors.add(actor)
        return JsonResponse({"MESSAGE": "CREATED"}, status=201)
