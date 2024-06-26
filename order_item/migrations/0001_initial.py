# Generated by Django 5.0.3 on 2024-04-13 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('products', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('order_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_id', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddConstraint(
            model_name='order_item',
            constraint=models.UniqueConstraint(fields=('order_id', 'product_id'), name='order_item_composite_key'),
        ),
    ]
