# Generated by Django 2.2 on 2021-07-31 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20210731_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='cart_id',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
