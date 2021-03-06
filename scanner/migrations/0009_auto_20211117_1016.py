# Generated by Django 3.2.9 on 2021-11-17 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0008_rencanakirimdetail_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rencanakirimdetail',
            name='barang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barangs', to='scanner.barang'),
        ),
        migrations.AlterField(
            model_name='rencanakirimdetail',
            name='rencana_kirim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rencanakirimdetails', to='scanner.rencanakirim'),
        ),
    ]
