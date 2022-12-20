# Generated by Django 4.1.3 on 2022-12-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0031_alter_barang_part_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rencanakirim',
            name='nomor_sj',
        ),
        migrations.AddField(
            model_name='rencanakirimdetail',
            name='pcs_scanned',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rencanakirimdetail',
            name='qty',
            field=models.CharField(max_length=4),
        ),
    ]
