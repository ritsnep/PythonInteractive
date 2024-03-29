# Generated by Django 5.0.1 on 2024-01-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesorder_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
    ]
