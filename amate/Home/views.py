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
        template_name = 'detail_Publication.html'
# class Detail_product(DetailView):
#     model = producto
#     template_name= 'detail_product.html'

# class Create_product(CreateView):
#     model = producto
#     template_name = 'create_products.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('detail_product', kwargs={'pk':self.object.pk})

# class Delete_product(DeleteView):
#     model = producto
#     template_name = 'delete_product.html'

#     def get_success_url(self):
#         return reverse('list_products')

# class Update_product(UpdateView):
#     model = producto
#     template_name = 'update_product.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('detail_product', kwargs = {'pk':self.object.pk})