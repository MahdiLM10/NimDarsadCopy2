# Generated by Django 5.1.2 on 2024-12-09 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0035_order_all_price_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 12, 9, 18, 51, 15, 760537)),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
