# Generated by Django 3.2.9 on 2021-11-11 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0002_auto_20211111_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='part_number',
            field=models.CharField(max_length=18),
        ),
    ]
