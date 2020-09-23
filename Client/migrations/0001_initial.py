# Generated by Django 3.1 on 2020-09-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Phone', models.IntegerField(blank=True)),
                ('pet_type', models.CharField(max_length=20)),
            ],
        ),
    ]