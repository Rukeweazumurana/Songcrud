from django.db import models
from datetime import datetime
# Create your models here.

class Artiste(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()

class Song(models.Model):
    artiste = models.OneToOneField(Artiste, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    date_released=models.DateField(default=datetime.today)
    likes=models.IntegerField()
    artiste_id=models.IntegerField()

class Lyric(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE)
    content=models.CharField(max_length=500)
    song_id=models.IntegerField()
