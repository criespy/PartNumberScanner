# Generated by Django 4.1.3 on 2022-12-19 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0032_remove_rencanakirim_nomor_sj_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rencanakirimdetail',
            name='box_scanned',
            field=models.IntegerField(default=0),
        ),
    ]
