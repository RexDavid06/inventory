from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Transaction

# This function automatically updates the stock levels after a transaction is saved
@receiver(post_save, sender=Transaction)
def update_stock(sender, instance, created, **kwargs):
    if created:
        if instance.transaction_type == 'IN':
            instance.product.quantity_in_stock += instance.quantity
        elif instance.transaction_type == 'OUT':
            instance.product.quantity_in_stock -= instance.quantity
        instance.product.save()
