# Generated by Django 3.2.9 on 2022-11-04 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0016_auto_20221102_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rencanakirimdetail',
            old_name='nomor_line',
            new_name='no_line',
        ),
    ]