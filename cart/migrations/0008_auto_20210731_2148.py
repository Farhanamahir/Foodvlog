# Generated by Django 2.2 on 2021-07-31 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20210731_1724'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cartlist',
            new_name='cartlists',
        ),
    ]