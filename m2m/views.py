from django.shortcuts import render
import json

from django.http import JsonResponse
from django.views import View
from m2m.models import Movie, Actor, Actor_Movie


class MovieView(View):
    def post(self, request):
        
        data = json.loads(request.body)
        Movie.objects.create(title=data['title'],
                             release_date=data['release_date'],
                             running_time=data['running_time'])
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

    def get(self, request):
        result = []
        actors = Actor.objects.all()

        for actor in actors:
            movie_list = []
            movies = actor.movie.all()

            for movie in movies:
                movie_list.append(movie.title)
            result.append(
                {
                    'last_name': actor.last_name,
                    'first_name': actor.first_name,
                    'movies': movie_list
                }
            )
        return JsonResponse({'result':result}, status=200)


class ActorView(View):
    def post(self, request):
        
        data = json.loads(request.body)
        Actor.objects.create(first_name=data['first_name'],
                             last_name=data['last_name'],
                             date_of_birth=data['date_of_birth'])
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

    def get(self, request):
        result = []
        movies = Movie.objects.all()

        for movie in movies:
            actor_list = []
            actors = movie.actor_set.all()

            for actor in actors:
                actor_list.append(actor.last_name +' '+actor.first_name)
            
            result.append(
                {
                    'title': movie.title,
                    'running_time': movie.running_time,
                    'actors': actor_list
                }
            )
        return JsonResponse({'result':result}, status=200)