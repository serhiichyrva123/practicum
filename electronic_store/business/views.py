
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.utils import extend_schema, extend_schema_view

from electronic_store.models import Product, Order, Invoice
from electronic_store.business.serializers import ProductSerializer, OrderSerializer, InvoiceSerializer
from electronic_store.business.permissions import IsCashier, IsConsultant, IsAccountant
from electronic_store.business.filters import OrderFilter


@extend_schema_view(
    list=extend_schema(summary="Список товарів", tags=["Товари"]),
    retrieve=extend_schema(summary="Деталі товару", tags=["Товари"]),
)
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Створити замовлення на товар",
        description="Створює замовлення на вибраний товар за його ідентифікатором",
        tags=["Товари"]
    )
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsCashier])
    def create_order(self, request, pk=None) -> Response:
        product = self.get_object()
        order = Order.objects.create(product=product)
        serializer = OrderSerializer(order)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema_view(
    list=extend_schema(summary="Список замовлень", tags=["Замовлення"]),
    retrieve=extend_schema(summary="Деталі замовлення", tags=["Замовлення"]),
    create=extend_schema(summary="Створити замовлення", tags=["Замовлення"]),
)
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    @extend_schema(
        summary="Змінити статус замовлення",
        description="Дозволяє встановити новий статус для замовлення за його ідентифікатором.",
        tags=["Замовлення"]
    )
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsCashier | IsConsultant])
    def set_status(self, request, pk=None) -> Response:
        order = self.get_object()
        new_status = request.data.get('status')

        if new_status not in dict(Order.CHOICES):
            return Response({'error': 'Некоректний статус 💀'}, status=status.HTTP_400_BAD_REQUEST)

        order.status = new_status
        order.save()

        return Response({'status': order.status})


@extend_schema_view(
    list=extend_schema(summary="Список накладних", tags=["Накладні"]),
    retrieve=extend_schema(summary="Деталі накладної", tags=["Накладні"]),
    create=extend_schema(summary="Створити накладну", tags=["Накладні"]),
)
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated, IsAccountant | IsCashier]