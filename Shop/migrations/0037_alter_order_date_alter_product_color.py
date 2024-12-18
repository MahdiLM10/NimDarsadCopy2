# Generated by Django 5.1.2 on 2024-12-09 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0036_alter_order_date_alter_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 12, 9, 18, 53, 51, 617328)),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
