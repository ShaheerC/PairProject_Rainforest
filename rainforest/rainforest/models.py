from django.db import models
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_in_cents = models.IntegerField()

    def __str__(self):
        return self.name

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price_in_cents']
