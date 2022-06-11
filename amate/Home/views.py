from django.shortcuts import render
from Home.models import Publicacion
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# Create your views here.


class List_publications(ListView):
    model = Publicacion
    template_name = 'index.html'
    queryset = Publicacion.objects.filter(active = True)

class Detail_publication(DetailView):
    model = Publicacion
    template_name = 'detail_publication.html'

class Create_publication(CreateView):
    model = Publicacion
    template_name = 'create_publication.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('detail_publication', kwargs={'pk':self.object.pk})

class Delete_publication(DeleteView):
    model = Publicacion
    template_name = 'delete_publication.html'
    def get_success_url(self):
        return reverse('list_publications')


class Update_publication(UpdateView):
    model = Publicacion
    template_name = 'update_publication.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_publication', kwargs = {'pk':self.object.pk})