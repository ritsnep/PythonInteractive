# Generated by Django 5.0.1 on 2024-01-30 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesorder_api', '0005_delete_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sales_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesorder_api.salesorder')),
            ],
        ),
    ]
