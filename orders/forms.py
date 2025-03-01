from django import forms
from .models import Order, Item
from django.forms import ModelMultipleChoiceField


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class OrderForm(forms.ModelForm):
    items = ModelMultipleChoiceField(queryset=Item.objects.all(), label="Блюда", widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Order
        fields = ['table_number', 'status', 'items']
