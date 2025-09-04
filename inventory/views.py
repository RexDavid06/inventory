from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Product, Category, Transaction
from .forms import ProductForm, ProductEditForm, CategoryForm
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Sum, Case, When, F


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


from django.views.generic import TemplateView
from django.db.models import Sum, F
from .models import Transaction, Product


from django.views.generic import TemplateView
from django.db.models import Sum, F
from .models import Product, Transaction


class ReportsView(TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        transactions = Transaction.objects.select_related("product").all().order_by("-date")

        report_data = []
        balance = {}

        for trx in transactions:
            product = trx.product

            # Initialize product balance if not set
            if product not in balance:
                balance[product] = 0

            # Adjust running balance correctly
            if trx.transaction_type == "IN":
                balance[product] += trx.quantity
            elif trx.transaction_type == "OUT":
                balance[product] -= trx.quantity

            report_data.append({
                "date": trx.date,
                "product": product.name,
                "qty_in": trx.quantity if trx.transaction_type == "IN" else 0,
                "qty_out": trx.quantity if trx.transaction_type == "OUT" else 0,
                "balance": balance[product]
            })


        # Totals across all products
        total_inflow = Transaction.objects.filter(transaction_type="IN").aggregate(total=Sum("quantity"))["total"] or 0
        total_outflow = Transaction.objects.filter(transaction_type="OUT").aggregate(total=Sum("quantity"))["total"] or 0

        # Dynamically compute stock value from transactions
        total_value = 0
        for product in Product.objects.all():
            inflow = Transaction.objects.filter(product=product, transaction_type="IN").aggregate(total=Sum("quantity"))["total"] or 0
            outflow = Transaction.objects.filter(product=product, transaction_type="OUT").aggregate(total=Sum("quantity"))["total"] or 0
            stock_balance = inflow - outflow
            total_value += stock_balance * (product.unit_price or 0)

        # Add to context
        context["records"] = report_data
        context["total_inflow"] = total_inflow
        context["total_outflow"] = total_outflow
        context["total_value"] = total_value

        return context



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

