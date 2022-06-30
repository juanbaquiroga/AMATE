from django.shortcuts import render
from Productos.models import producto, categoria
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.

# class List_products1(ListView):
#         model = producto
#         template_name = 'products.html'
#         queryset = producto.objects.filter(active = True), categoria.objects.filter(name = True)

def list_products(request):
    productos = producto.objects.all()
    categorias = categoria.objects.all()
    context = {'productos':productos, 'categorias':categorias}
    return render(request, 'productos/products.html', context=context)

class Detail_product(DetailView):
    model = producto
    template_name= 'productos/detail_product.html'

class Create_product(CreateView):
    model = producto
    template_name = 'productos/create_products.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk':self.object.pk})

class Delete_product(DeleteView):
    model = producto
    template_name = 'productos/delete_product.html'

    def get_success_url(self):
        return reverse('List_products')

class Update_product(UpdateView):
    model = producto
    template_name = 'productos/update_product.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_product', kwargs = {'pk':self.object.pk})


def search_product(request):
    productos = producto.objects.filter(name__icontains = request.GET['search'])
    if productos.exists():
        context = {'productos':productos}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'productos/search_product.html', context = context)


