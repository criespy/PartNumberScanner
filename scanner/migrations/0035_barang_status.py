# Generated by Django 4.1.3 on 2023-03-07 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0034_alter_barang_qty_per_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='status',
            field=models.CharField(choices=[('Aktif', 'Aktif'), ('Disabled', 'Disabled')], default='Aktif', max_length=8),
        ),
    ]