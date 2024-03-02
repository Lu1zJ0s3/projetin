
from django.db import models

class veiculos(models.Model):
    nome=models.CharField(max_length=100)
    cor=models.CharField(max_length=100)
    montadora=models.CharField(max_length=100)