from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Product, Category
from .forms import ProductForm
from django.urls import reverse_lazy

#Create your views here.
class IndexView(TemplateView):
    template_name = "inventory/index.html"


class HomeView(ListView):
    queryset = Product.objects.all()
    template_name = 'inventory/home.html'
    context_object_name = 'products'


class DashboardView(TemplateView):
    template_name = 'inventory/dashboard.html'


class AddItemView(CreateView):
    model = Product
    template_name = 'inventory/add-item.html'
    form_class = ProductForm
    success_url = reverse_lazy('inventory:home')


class ReportsView(TemplateView):
    template_name = 'inventory/reports.html'
