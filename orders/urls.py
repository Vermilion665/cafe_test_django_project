from django.shortcuts import render
from django.urls import include, path
from .views import MoneyPaidView, OrderCreateView, OrderDetailView, OrderListView, index, ItemCreateView, ItemListView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/items', views.ItemViewSet, basename='api-items')
router.register(r'api/orders', views.OrderViewSet, basename='api-orders')


app_name = 'orders'
urlpatterns = [
    path('', index, name='index'),
    path('item-form/', ItemCreateView.as_view(), name='item-form'),
    path('item-list/', ItemListView.as_view(), name='item-list'),
    path('order-form/', OrderCreateView.as_view(), name='order-form'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('order-detail/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('money-paid/', MoneyPaidView.as_view(), name='money-paid'),
    path('api/', include(router.urls)),
]