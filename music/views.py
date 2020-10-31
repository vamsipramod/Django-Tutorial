from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = "music/index.html"

    #Default variable name that is sent to template will be object_list
    #to change the variable name set 'context_object_name' to desired variable name
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailsView(generic.DetailView):
    template_name = "music/detail.html"
    model = Album


#ModelForms Simplest way to create forms
#It automatically genreate form html, adds the forms requests to database automatically
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
