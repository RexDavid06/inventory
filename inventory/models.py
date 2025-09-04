from django.db import models
from django.db.models import Sum, F

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='products'
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=1)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10)  # Alert Level
    created_at = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(
        "Supplier",
        on_delete=models.SET_NULL,  # if supplier deleted, product remains but supplier becomes NULL
        null=True,
        related_name="products"
    )
    
    def total_value(self):
        """gets the total stock value of a particular product"""
        return self.unit_price * self.quantity_in_stock
    
    @classmethod
    def total_products(cls):
        """gets the total number of products in the business"""
        return cls.objects.count()
    
    @classmethod
    def total_stock_value(cls):
        """gets the total stock value of the total products in business"""
        result = cls.objects.aggregate(
            total_value = Sum(F("unit_price") * F("quantity_in_stock"))
        )
        return result["total_value"] or 0

    def __str__(self):
        return self.name


class Supplier(models.Model):
    company_name = models.CharField(max_length=255, blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField()

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.company_name
    



class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=200, blank=True, null=True)  # e.g. "Sold", "Damaged"

    def __str__(self):
        return f"{self.product.name} - {self.transaction_type} - {self.quantity}"

    @property
    def total_value(self):
        """Monetary value of this transaction"""
        return self.quantity * self.product.unit_price

    

