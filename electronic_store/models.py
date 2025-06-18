
from django.db import models
from django.db.models import DecimalField
from django.utils import timezone

from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta

# TODO: додати перевірку mypy?


class Product(models.Model):
    name: str = models.CharField(max_length=255, verbose_name="Назва продукту")
    price: Decimal = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Ціна")
    created_at: datetime = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")

    @property
    def has_discount(self) -> bool:
        return self.created_at.date() < (timezone.now().date() - relativedelta(months=1))

    @property
    def price_at_order(self) -> Decimal | DecimalField:
        if self.has_discount:
            return self.price * Decimal('0.80')
        return self.price

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"
        db_table = "products"


class Order(models.Model):
    CHOICES = [("created", "Нове"), ("paid", "Оплачене"), ("completed", "Виконане")]

    product: Product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Замовлений продукт")
    status: str = models.CharField(max_length=30, choices=CHOICES, default="created", verbose_name="Статус замовлення")
    created_at: datetime = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")

    def __str__(self) -> str:
        return f"Замовлення №{self.id} - {self.product.name}"

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
        db_table = "orders"


class Invoice(models.Model):
    order: Order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name="Замовлення")
    created_at: datetime = models.DateTimeField(auto_now_add=True, verbose_name="Дата накладної")

    def __str__(self) -> str:
        return f"Накладна замовлення №{self.order.id}"

    class Meta:
        verbose_name = "Накладна"
        verbose_name_plural = "Накладні"
        db_table = "invoices"