# views.py

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Delivery
from .serializers import DeliverySerializer

class DeliveryCreateView(generics.CreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]

class DeliveryDetailView(generics.RetrieveAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class DeliveryUpdateView(generics.UpdateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class OrderDeliveryDetailView(generics.RetrieveAPIView):
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        order_id = self.kwargs['orderId']
        try:
            return Delivery.objects.get(order__id=order_id)
        except Delivery.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        delivery = self.get_object()
        if delivery is None:
            return Response(
                {"detail": f"Delivery for order {self.kwargs['orderId']} does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(delivery)
        return Response(serializer.data)
