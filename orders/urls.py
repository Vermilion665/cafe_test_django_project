from django.shortcuts import render
from django.urls import path
from .views import OrderCreateView, OrderListView, index, ItemCreateView, ItemListView


app_name = 'orders'
urlpatterns = [
    path('', index, name='index'),
    path('item-form/', ItemCreateView.as_view(), name='item-form'),
    path('item-list/', ItemListView.as_view(), name='item-list'),
    path('order-form/', OrderCreateView.as_view(), name='order-form'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    # path('order-delete/', order_delete, name='order-delete'),
    # path('order-found/', order-found, name='order-found'),
    # path('order-update/', order_update, name='order-update'),
]