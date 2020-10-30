from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = "music/index.html"

    #Default variable name that is sent to template will be object_list
    #to change the variable name set 'context_object_name' to desired variable name
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailsView(generic.DetailView):
    template_name = "music/detail.html"
    model = Album



