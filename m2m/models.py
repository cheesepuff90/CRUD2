from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movies'

class Actor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    movie = models.ManyToManyField('Movie', through = 'Actor_Movie')

    class Meta:
        db_table = 'actors'

class Actor_Movie(models.Model):
    actor_id = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actor_movies'