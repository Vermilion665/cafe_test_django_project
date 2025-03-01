from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView
from .models import Item, Order
from .forms import ItemForm, OrderForm
from django.urls import reverse_lazy


def index(request):
    return render(request, 'orders/base.html')


class ItemCreateView(CreateView):
    model = Item
    fields = '__all__'
    form = ItemForm
    template_name = 'orders/item-form.html'
    success_url = reverse_lazy('orders:item-list')


class ItemListView(ListView):
    model = Item
    template_name = 'orders/item-list.html'
    context_object_name = 'items'


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order-form.html'
    success_url = reverse_lazy('orders:order-list')

    def form_valid(self, form):
        order = form.save()
        order.total_price = order.calculate_total_price()
        order.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order-list.html'
    context_object_name = 'orders'


class OrderDetailView(View):
    pass