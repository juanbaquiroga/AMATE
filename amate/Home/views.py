from django.shortcuts import render
from Home.models import Publicacion
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# Create your views here.


class Publications_list(ListView):
        model = Publicacion
        template_name = 'index.html'
        queryset = Publicacion.objects.filter(active = True)

class Detail_Publication(DetailView):
        model = Publicacion
        template_name = 'home/detail_publication.html'

class Create_Publication(CreateView):
    model = Publicacion
    template_name = 'home/create_publication.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail-publication', kwargs={'pk':self.object.pk})

class Delete_Publication(DeleteView):
    model = Publicacion
    template_name = 'home/delete_publication.html'

    def get_success_url(self):
        return reverse('home')

class Update_Publication(UpdateView):
    model = Publicacion
    template_name = 'home/update_publication.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail-publication', kwargs = {'pk':self.object.pk})


def about_us(request):
    return render(request, 'home/about_us.html', context = {})