# Generated by Django 4.2.3 on 2023-08-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0005_rename_name_order_status_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_status',
            name='order_status',
            field=models.CharField(max_length=100),
        ),
    ]
