from django.db import models

class Barang(models.Model):
    part_number = models.CharField(max_length=18)
    description = models.CharField(max_length=32)
    barcode = models.TextField()

    def __str__(self):
        return self.part_number
