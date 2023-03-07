from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse, resolve
from django.core.validators import MaxValueValidator, MinValueValidator

class Barang(models.Model):
    part_number = models.CharField(max_length=18)
    description = models.CharField(max_length=32)
    part_number_customer =  models.CharField(max_length=18, unique=True)
    barcode = models.TextField(blank=True)
    color_code = models.CharField(max_length=3, blank=True, null=True)
    position_code = models.CharField(max_length=6, blank=True, null=True)
    qty_per_box = models.IntegerField(null=True, blank=True)
    class Status(models.TextChoices):
        AKTIF = 'Aktif',_('Aktif')
        DISABLED = 'Disabled',_('Disabled')
    status = models.CharField(max_length=8, choices=Status.choices, default=Status.AKTIF)

    def __str__(self):
        return self.part_number + " | " + self.part_number_customer + " | " + self.description

    def get_absolute_url(self):
        return reverse('list_barang')

class RencanaKirim(models.Model):
    #nomor_sj = models.CharField(max_length=7)
    tanggal = models.DateField()
    jam = models.TimeField(null=True, blank=True)
    cycle = models.IntegerField(validators=[MaxValueValidator(20),MinValueValidator(1)])
    class Status(models.TextChoices):
        OPEN = 'Open',_('Open')
        SCANNED = 'Scanned',_('Scanned')
    status = models.CharField(max_length=7, choices=Status.choices, default=Status.OPEN)
    #nomor_line = models.CharField(max_length=2)

    def __str__(self):
        return str(self.tanggal) + " C" + str(self.cycle)

    #url setelah update data
    def get_absolute_url(self):
        #currenturl = HttpRequest.get_host(self)
        #if(currenturl == [os.path.join(BASE_DIR, 'buat_rencana_kirim')]):
        #    return reverse('buat_rencana_kirim_detail', args=[str(self.id)])
        #else:
            #return reverse('delivery', args=[str(self.id)])
        return reverse('view_rencana_kirim')



class RencanaKirimDetail(models.Model):
    no_line = models.CharField(max_length=2, null=False, blank=False)
    rencana_kirim = models.ForeignKey(RencanaKirim, on_delete=models.CASCADE, related_name='rencanakirim')
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE, related_name='barang')
    qty = models.CharField(max_length=4, null=False, blank=False)
    box_scanned = models.IntegerField(default=0)
    pcs_scanned = models.IntegerField(default=0)
    #qty_per_pkg = models.IntegerField()

    def __str__(self):
        return str(self.no_line) + "-" + str(self.rencana_kirim)

    def get_absolute_url(self):
        return reverse('buat_rencana_kirim')

class Pengiriman(models.Model):
    no_pengiriman = models.IntegerField()
    waktu_kirim = models.DateTimeField()
    rencana_kirim = models.ForeignKey(RencanaKirim, on_delete=models.CASCADE)

    