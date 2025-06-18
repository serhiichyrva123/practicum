
from decimal import Decimal
from datetime import timedelta

from django.utils import timezone
from django.core.management.base import BaseCommand

from electronic_store.settings import DEBUG
from electronic_store.models import Product, Order, Invoice


def create_fixtures():
    if DEBUG:
        Invoice.objects.all().delete()
        Order.objects.all().delete()
        Product.objects.all().delete()

    now = timezone.now()

    products = [
        Product.objects.create(name="Ноутбук Lenovo", price=Decimal("27000.00"), created_at=now - timedelta(days=10)),
        Product.objects.create(name="Смартфон Samsung", price=Decimal("18000.00"), created_at=now - timedelta(days=5)),
        Product.objects.create(name="Навушники Sony", price=Decimal("3200.00"), created_at=now - timedelta(days=1)),
        Product.objects.create(name="Монітор LG", price=Decimal("8500.00"), created_at=now - timedelta(days=40)),
        Product.objects.create(name="Клавіатура Logitech", price=Decimal("2300.00"), created_at=now - timedelta(days=50)),
        Product.objects.create(name="Миша Razer", price=Decimal("1900.00"), created_at=now - timedelta(days=70)),
    ]

    orders = [
        Order.objects.create(product=products[0], status="created"),
        Order.objects.create(product=products[3], status="paid"),
        Order.objects.create(product=products[5], status="completed"),
    ]

    invoices = [
        Invoice.objects.create(order=orders[1]),
        Invoice.objects.create(order=orders[2]),
    ]


class Command(BaseCommand):
    help = "завантажує тестові фікстури для перевірки магазину"

    def handle(self, *args, **options):
        create_fixtures()
        self.stdout.write(self.style.SUCCESS("фікстури успішно завантажено"))
