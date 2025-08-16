from django.contrib import admin
from .models import Product,  Category, Supplier, StockIn, StockOut

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(StockOut)
admin.site.register(StockIn)
