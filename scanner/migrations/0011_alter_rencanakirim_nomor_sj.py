# Generated by Django 3.2.9 on 2021-11-21 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0010_alter_rencanakirim_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rencanakirim',
            name='nomor_sj',
            field=models.IntegerField(max_length=6),
        ),
    ]