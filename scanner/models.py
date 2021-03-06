from django.db import models
from django.http import request, HttpRequest
from django.utils.translation import gettext_lazy as _
from django.urls import reverse, resolve

class Barang(models.Model):
    part_number = models.CharField(max_length=18)
    description = models.CharField(max_length=32)
    part_number_customer =  models.CharField(max_length=18)
    barcode = models.TextField()

    def __str__(self):
        return self.part_number + " == " + self.description

class RencanaKirim(models.Model):
    nomor_sj = models.CharField(max_length=6, unique=True)
    tanggal = models.DateTimeField()
    class Status(models.TextChoices):
        OPEN = 'Open',_('Open')
        SCANNED = 'Scanned',_('Scanned')
    status = models.CharField(max_length=7, choices=Status.choices, default=Status.OPEN)
    #nomor_line = models.CharField(max_length=2)

    def __str__(self):
        return self.nomor_sj

    #url setelah update data
    def get_absolute_url(self):
        #currenturl = HttpRequest.get_host(self)
        #if(currenturl == [os.path.join(BASE_DIR, 'buat_rencana_kirim')]):
        #    return reverse('buat_rencana_kirim_detail', args=[str(self.id)])
        #else:
            return reverse('delivery', args=[str(self.id)])



class RencanaKirimDetail(models.Model):
    nomor_line = models.CharField(max_length=2)
    rencana_kirim = models.ForeignKey(RencanaKirim, on_delete=models.CASCADE, related_name='rencanakirimdetails')
    barang= models.ForeignKey(Barang, on_delete=models.CASCADE, related_name='barangs')
    qty = models.CharField(max_length=2)

    def __str__(self):
        return self.rencana_kirim.nomor_sj

    def get_absolute_url(self):
        return reverse('buat_rencana_kirim')
