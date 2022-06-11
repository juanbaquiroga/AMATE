from django.shortcuts import render
from Productos.models import producto, categoria
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.

# PRODUCTOS
class List_products(ListView):
        model = producto
        template_name = 'products.html'
        queryset = producto.objects.filter(active = True)

class Detail_product(DetailView):
    model = producto
    template_name= 'detail_product.html'

class Create_product(CreateView):
    model = producto
    template_name = 'create_products.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk':self.object.pk})

class Delete_product(DeleteView):
    model = producto
    template_name = 'delete_product.html'

    def get_success_url(self):
        return reverse('list_products')

class Update_product(UpdateView):
    model = producto
    template_name = 'update_product.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_product', kwargs = {'pk':self.object.pk})

def search_product(request):
    productos = producto.objects.filter(name__icontains = request.GET['search'])
    if productos.exists():
        context = {'productos':productos}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'search_product.html', context = context)

# CATEGORIAS

class List_category(ListView):
        model = categoria
        template_name = 'category.html'

class Create_category(CreateView):
    model = categoria
    template_name = 'create_category.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('list_category')

class Delete_category(DeleteView):
    model = categoria
    template_name = 'delete_category.html'

    def get_success_url(self):
        return reverse('list_category')

class Update_category(UpdateView):
    model = categoria
    template_name = 'update_category.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('list_category')