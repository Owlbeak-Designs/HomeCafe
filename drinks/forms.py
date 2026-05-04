from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['drink_type']
        widgets = {
            'drink_type': forms.Select(
                attrs = { 
                    'class': 'form-control'
                }
            )
        }
        labels = {
            'drink_type': 'Select your drink'
        }