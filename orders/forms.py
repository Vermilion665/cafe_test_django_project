from django import forms
from .models import Order, Item

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items', 'status']
        widgets = {
            'items': forms.CheckboxSelectMultiple(),
        }