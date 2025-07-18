# Generated by Django 5.2.3 on 2025-06-18 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'Нове'), ('paid', 'Оплачене'), ('completed', 'Виконане')], default='created', max_length=30, verbose_name='Статус замовлення')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата замовлення')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва продукту')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Ціна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Час створення')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукти',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата накладної')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='electronic_store.order', verbose_name='Замовлення')),
            ],
            options={
                'verbose_name': 'Накладна',
                'verbose_name_plural': 'Накладні',
                'db_table': 'invoices',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='electronic_store.product', verbose_name='Замовлений продукт'),
        ),
    ]
