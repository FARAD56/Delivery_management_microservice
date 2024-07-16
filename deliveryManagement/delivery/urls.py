# urls.py

from django.urls import path
from .views import DeliveryCreateView, DeliveryDetailView, DeliveryUpdateView, OrderDeliveryDetailView

urlpatterns = [
    path('deliveries/create', DeliveryCreateView.as_view(), name='delivery-create'),
    path('deliveries/<int:id>', DeliveryDetailView.as_view(), name='delivery-detail'),
    path('deliveries/update/<int:id>', DeliveryUpdateView.as_view(), name='delivery-update'),
    path('orders/<int:orderId>/deliveries', OrderDeliveryDetailView.as_view(), name='order-delivery-detail'),
]
