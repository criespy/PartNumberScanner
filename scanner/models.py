from django.db import models
from django.utils.translation import gettext_lazy as _

class Barang(models.Model):
    part_number = models.CharField(max_length=18)
    description = models.CharField(max_length=32)
    part_number_customer =  models.CharField(max_length=18)
    barcode = models.TextField()

    def __str__(self):
        return self.part_number

class RencanaKirim(models.Model):
    nomor_sj = models.CharField(max_length=6)
    tanggal = models.DateTimeField()
    class Status(models.TextChoices):
        OPEN = 'OP',_('Open')
        SCANNED = 'SC',_('Scanned')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.OPEN)
    #nomor_line = models.CharField(max_length=2)

    def __str__(self):
        return self.nomor_sj

class RencanaKirimDetail(models.Model):
    nomor_line = models.CharField(max_length=2)
    rencana_kirim = models.ForeignKey(RencanaKirim, on_delete=models.CASCADE, related_name='rencanakirimdetails')
    barang= models.ForeignKey(Barang, on_delete=models.CASCADE, related_name='barangs')
    qty = models.CharField(max_length=2)

    def __str__(self):
        return self.rencana_kirim.nomor_sj
