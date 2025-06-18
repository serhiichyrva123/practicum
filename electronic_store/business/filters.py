
from django_filters import DateFilter, FilterSet

from electronic_store.models import Order


class OrderFilter(FilterSet):
    created_at_after = DateFilter(field_name='created_at', lookup_expr='gte')
    created_at_before = DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['created_at_after', 'created_at_before']
