# Generated by Django 4.1.3 on 2022-11-15 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0025_alter_barang_part_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='barcode',
            field=models.TextField(unique=True),
        ),
    ]
