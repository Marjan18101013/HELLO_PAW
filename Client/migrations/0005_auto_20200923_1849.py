# Generated by Django 3.1 on 2020-09-23 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PetService', '0001_initial'),
        ('Client', '0004_auto_20200923_1846'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer_service',
            new_name='CustomerService',
        ),
    ]