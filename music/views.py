from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import  generic
from django.views.generic import View
from .forms import UserForm
from .models import Album


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


class UserFormView(View):
    form_class = UserForm
    template_name = "music/registration_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned Normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return USer object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        return render(request, self.template_name, {'form': form})