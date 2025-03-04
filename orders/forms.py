from django import forms
from .models import Order, Item
from django.forms import ModelMultipleChoiceField


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'dish_name': forms.TextInput(attrs={'class': 'my-custom-item-input'}),
            'price': forms.NumberInput(attrs={'class': 'my-custom-item-input', 'min':'1'}),
        }


class OrderForm(forms.ModelForm):
    items = ModelMultipleChoiceField(queryset=Item.objects.all(), label="Блюда", widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Order
        fields = ['table_number', 'status', 'items']
        widgets = {
            'table_number': forms.NumberInput(attrs={'class': 'my-custom-input', 'min':'1'}),
            'status': forms.Select(attrs={'class': 'my-custom-select'}),
        }


class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'my-custom-select'}),
        }