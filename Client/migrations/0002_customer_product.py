# Generated by Django 3.1 on 2020-09-23 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PetShop', '0002_product_b_id'),
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Client.customer')),
                ('p_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PetShop.product')),
            ],
        ),
    ]
