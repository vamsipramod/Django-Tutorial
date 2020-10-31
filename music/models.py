# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

"""
When ever the server first gets booted up, It checks the settings.py > INSTALLED APPS and for each
installed app it checks whether app's model reflects the same in database.
"""

"""
Steps to do whenever you make a change to the app's model.py:
1. $ python manage.py makemigrations app_name  // Create's a file in migrations which contains commands
                                                to reflects change to database
2. $ python manage.py migrate        //runs the files in migrations to reflect changes to database

Note: In case you want to view file in migrations 
     $ python manage.py sqlmigrate app_name file_name
"""

"""
Whenever you create a new app you must add its model to settings.py > INSTALLED_APPS 
and Register the model in admin.py 
"""
# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.album_title + '-' + self.artist + '-' + self.genre


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    filetype = models.CharField(max_length=20)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

#Simplest way to create an Song and link with album
# album = Album.object.get(pk=some_id)
# album.song_set.create(filetype='mp3',song_title='abc') all fields must be passed
