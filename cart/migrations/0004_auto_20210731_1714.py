# Generated by Django 2.2 on 2021-07-31 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_items_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='cart_id',
            field=models.CharField(max_length=250, null=True, unique=True),
        ),
    ]
