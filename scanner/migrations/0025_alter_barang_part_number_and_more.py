# Generated by Django 4.1.3 on 2022-11-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0024_alter_rencanakirim_nomor_sj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='part_number',
            field=models.CharField(max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name='barang',
            name='part_number_customer',
            field=models.CharField(max_length=18, unique=True),
        ),
    ]
