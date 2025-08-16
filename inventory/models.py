from django.db import models

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    unit_price = models.DecimalField(max_digits=10, decimal_places=1)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10) # Alert Level
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

    def total_value(self):
        return self.unit_price * self.quantity_in_stock

    def __str__(self):
        return self.name


class StockIn(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stockin')
    quantity = models.PositiveIntegerField()
    supplier = models.ForeignKey("Supplier", on_delete=models.SET_NULL, null=True)
    stocked_at = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Stock In'
        verbose_name_plural = 'Stocks In'
        ordering = ['-stocked_at']

    def __str__(self):
        return f"{self.quantity} of {self.product.name} stocked at {self.stocked_at}"    
    
    
class StockOut(models.Model):
    REASONS = (
        ("sold", "Sold"),
        ("damaged", "Damaged"),
        ("company", "Company Use")
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stockout')
    quantity = models.PositiveIntegerField()
    reason = models.CharField(max_length=255, choices=REASONS)

    class Meta:
        verbose_name = 'Stock Out'
        verbose_name_plural = 'Stocks Out'

    def __str__(self):
        return f"Total number of {self.product} sold is {self.quantity}"


class Supplier(models.Model):
    company_name = models.CharField(max_length=255, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField()

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
    

    def __str__(self):
        return f"Supplier: {self.company_name}\nSupplies: {self.product}"
    


    

