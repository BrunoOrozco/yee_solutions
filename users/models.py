from django.contrib.auth.models import User
from django.db import models


class Vendedores(models.Model):
    """Modelo para DB de los vendedores"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendedor_user', primary_key=True)
    username = models.CharField(max_length=100)
    categoria = models.CharField(max_length=150, blank=True, null=True)
    lider = models.CharField(max_length=150, blank=True, null=True)
    region = models.CharField(max_length=150, blank=True, null=True)
    modified = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "usuarios"

        verbose_name = "vendedor"
    
    def __str__(self):
        return self.username




