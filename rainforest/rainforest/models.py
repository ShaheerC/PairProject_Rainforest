from django.db import models
from django.forms import ModelForm
from django.core.validators import URLValidator, MinLengthValidator, MaxLengthValidator
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
        fields = ["name", "description", "price_in_cents"]

    def clean(self):
       cleaned_data = super().clean()
       description = cleaned_data.get('description')
       price_in_cents = cleaned_data.get('price_in_cents')
       if description == None:
           pass
       elif len(description) <= 10 or len(description) >=500:
           self.add_error('description', 'Description must be between 10 and 500 characters long')