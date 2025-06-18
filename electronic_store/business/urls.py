
from django.urls import path

from electronic_store.business.views import ProductViewSet, OrderViewSet, InvoiceViewSet


product_list = ProductViewSet.as_view({'get': 'list'})
product_detail = ProductViewSet.as_view({'get': 'retrieve'})
product_create_order = ProductViewSet.as_view({'post': 'create_order'})

order_list = OrderViewSet.as_view({'get': 'list'})
order_detail = OrderViewSet.as_view({'get': 'retrieve'})
order_create = OrderViewSet.as_view({'post': 'create'})
order_set_status = OrderViewSet.as_view({'post': 'set_status'})

invoice_list = InvoiceViewSet.as_view({'get': 'list'})
invoice_detail = InvoiceViewSet.as_view({'get': 'retrieve'})
invoice_create = InvoiceViewSet.as_view({'post': 'create'})


urlpatterns = [
    path('products/list/', product_list, name='product-list'),
    path('products/detail/<int:pk>/', product_detail, name='product-detail'),
    path('products/<int:pk>/create_order/', product_create_order, name='product-create-order'),

    path('orders/list/', order_list, name='order-list'),
    path('orders/detail/<int:pk>/', order_detail, name='order-detail'),
    path('orders/create_order/', order_create, name='order-create'),
    path('orders/<int:pk>/set_status/', order_set_status, name='order-set-status'),

    path('invoices/list/', invoice_list, name='invoice-list'),
    path('invoices/detail/<int:pk>/', invoice_detail, name='invoice-detail'),
    path('invoices/create_invoice/', invoice_create, name='invoice-create')
]
