# Generated by Django 5.1.6 on 2025-03-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_item_price_alter_order_table_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=8, verbose_name='Цена'),
        ),
    ]
