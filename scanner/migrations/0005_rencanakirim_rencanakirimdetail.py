# Generated by Django 3.2.9 on 2021-11-15 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0004_barang_part_number_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='RencanaKirim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_sj', models.CharField(max_length=6)),
                ('tanggal', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RencanaKirimDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanner.barang')),
                ('rencana_kirim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanner.rencanakirim')),
            ],
        ),
    ]
