from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from .models import Item, Order, reverse_status_map
from .forms import ItemForm, OrderForm, OrderStatusForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
from rest_framework import viewsets
from .serializers import ItemSerializer, OrderSerializer


def index(request):
    order = Order.objects.all()
    context = {
        'order_list': order
    }
    return render(request, 'orders/index.html', context=context)


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
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


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order-list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '').strip().lower()

        if search_query:
            try:
                table_number = int(search_query)
                queryset = queryset.filter(table_number=table_number)
            except ValueError:
                latin_status = reverse_status_map.get(search_query)
                if latin_status:
                    queryset = queryset.filter(status=latin_status)
                else:
                    queryset = queryset.filter(status__icontains=search_query)
        return queryset


class OrderDetailView(UpdateView):
    model = Order
    fields = ['status']
    template_name = 'orders/order-detail.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderStatusForm(instance=self.object)
        return context
    
    def post(self, request, *args, **kwargs):
        order = self.get_object()
        form = OrderStatusForm(request.POST, instance=order)
        form.save()
        if 'delete' in request.POST:
            order = self.get_object()
            order.delete()
            messages.success(request, "Заказ успешно удален!") 
            return redirect('orders:order-list') 
        return redirect(self.get_object().get_absolute_url())


class MoneyPaidView(TemplateView):
    template_name = 'orders/money-paid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_money_paid = Order.objects.filter(status='paid').aggregate(total=Sum('total_price'))['total'] or 0.00
        context['total_money_paid'] = total_money_paid
        return context
    

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer