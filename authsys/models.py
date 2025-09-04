from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    ROLES = (
        ("sales", "Sales Representative"),
        ("driver", "Driver"),
        ("inventory", "Inventory Staff"),
        ("inventory manager", "Inventory Manager"),
        ("logistics manager", "Logistics Manager"),
        ("sales manager", "Sales Manager"),
    )

    role = models.CharField(max_length=30, choices=ROLES, blank=True, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # still required when using AbstractUser

    def __str__(self):
        return f"{self.email} ({self.role})"

    
