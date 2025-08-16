from django.db import models
from django.contrib.auth.models import User as DefaultUser


class User(models.Model):
    ROLES = (
        ("sales", "Sales Representative"),
        ("driver", "Driver"),
        ("inventory", "Inventory Staff"),
        ("inventory manager", "Inventory Manager"),
        ("logistics manager", "Logistics Manager" ),
        ("sale manager", "Sales Manager",)
    )
    user = models.OneToOneField(DefaultUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=ROLES)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
   
    
    def __str__(self):
        return self.role
    
    
