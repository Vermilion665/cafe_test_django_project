from django.urls import path
from .views import index

app_name = 'orders'
urlpatterns = [
    path('', index, name='index'),
    # path('order-create/', order_create, name='order-create'),
    # path('order-delete/', order_delete, name='order-delete'),
    # path('order-found/', order-found, name='order-found'),
    # path('order-list/', order_list, name='order-list'),
    # path('order-update/', order_update, name='order-update'),
]