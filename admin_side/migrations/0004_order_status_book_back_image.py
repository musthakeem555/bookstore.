# Generated by Django 4.2.3 on 2023-08-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0003_book_featured_book_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='back_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/book_covers'),
        ),
    ]
