from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Product, Category
from .forms import ProductForm, ProductEditForm, CategoryForm
from django.urls import reverse_lazy
from django.views import View

#Create your views here.
class IndexView(TemplateView):
    template_name = "inventory/index.html"


class HomeView(ListView):
    queryset = Product.objects.all()
    template_name = 'inventory/home.html'
    context_object_name = 'products'


class DashboardView(View):
    def get(self, request):
        total_products = Product.total_products
        total_stock_value = Product.total_stock_value
        context = {
            "total_products": total_products,
            "total_stock_value": total_stock_value,
        }
        return render(request, 'inventory/dashboard.html', context)
    



class AddItemView(CreateView):
    model = Product
    template_name = 'inventory/add-item.html'
    form_class = ProductForm
    success_url = reverse_lazy('inventory:home')


class ReportsView(TemplateView):
    template_name = 'inventory/reports.html'


class EditItemView(View):
    """ I intentional didn't use the built-in UpdateView here,
      because i was trying to have the under ground logic in my bones.
    I forgot it when thinking about it so i used methods instead """
    
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        edit_form = ProductEditForm(instance=product)
        context = {
            "form": edit_form,
            "product": product
        }
        return render(request, 'inventory/edit-item.html', context)
    
    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        edit_form = ProductEditForm(request.POST, instance=product)
        if edit_form.is_valid():
            edit_form.save()
            return redirect("inventory:home")
    

class DeleteItemView(View):
        def get(self, request, pk):
            product = Product.objects.get(pk=pk)
            return render(request, "inventory/delete-item.html", {"product": product})
        
        def post(self, request, pk):
            product = Product.objects.get(pk=pk)
            product.delete()
            return redirect("inventory:home")
        

class CategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventory/category.html'
    success_url = reverse_lazy('inventory:add-item')    
