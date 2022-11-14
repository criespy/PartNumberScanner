from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse, resolve
from django.core.validators import MaxValueValidator, MinValueValidator

class Barang(models.Model):
    part_number = models.CharField(max_length=18)
    description = models.CharField(max_length=32)
    part_number_customer =  models.CharField(max_length=18)
    barcode = models.TextField()
    color_code = models.CharField(max_length=3, blank=True, null=True)
    position_code = models.CharField(max_length=6, blank=True, null=True)
    qty_per_box = models.IntegerField(null=True)

    def __str__(self):
        return self.part_number + " == " + self.description

    def get_absolute_url(self):
        return reverse('list_barang')

class RencanaKirim(models.Model):
    nomor_sj = models.CharField(max_length=7, unique=True)
    tanggal = models.DateField()
    jam = models.TimeField(null=True, blank=True)
    cycle = models.IntegerField(validators=[MaxValueValidator(20),MinValueValidator(1)])
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
    no_line = models.CharField(max_length=2)
    rencana_kirim = models.ForeignKey(RencanaKirim, on_delete=models.CASCADE, related_name='rencanakirimdetails')
    barang= models.ForeignKey(Barang, on_delete=models.CASCADE, related_name='barangs')
    qty = models.CharField(max_length=2)
    #qty_per_pkg = models.IntegerField()

    def __str__(self):
        return self.rencana_kirim.nomor_sj

    def get_absolute_url(self):
        return reverse('buat_rencana_kirim')

class Pengiriman(models.Model):
    no_pengiriman = models.IntegerField()
    waktu_kirim = models.DateTimeField()
    rencana_kirim = models.ForeignKey(RencanaKirim, on_delete=models.CASCADE)
    