# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.http import HttpResponse
from .models import Album,Song
from django.template import loader
from django.shortcuts import render, get_object_or_404
# Create your views here.


def index(request):
    all_albums = Album.objects.all()

    # This  below method is not preferred
    # html = ''
    #
    # for album in all_albums:
    #     url = '/music/' + str(album.id) + "/"
    #     html += '<a href= "'+url+'">'+ album.album_title + '</a><br>'
    #
    # return HttpResponse(html)

    # Using Templates is the preferred method
    template = loader.get_template("music/index.html")
    context = {
        'all_albums' : all_albums
    }
    return HttpResponse(template.render(context, request))

# Note: We should always send a dictionary to the template


# shortcut method to return a HttpResponse
def detail(request, album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album Does not exist")
    #Alternative shortcut for above try-except logic

    album = get_object_or_404(Album,pk=album_id)

    return render(request, "music/detail.html", {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, "music/detail.html", {
            'album': album,
            'error_message': "You did not select valid song"
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, "music/detail.html", {'album': album})



