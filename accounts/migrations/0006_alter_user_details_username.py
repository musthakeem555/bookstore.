# Generated by Django 4.2.3 on 2023-07-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_details_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
