from django.db import models
from user.models import User
from buku.models import Buku

# Create your models here.

class StatusTransaksi(models.Model):
	nama = models.CharField(max_length=40)
	def __str__(self):
		return self.nama

class Transaksi(models.Model):
	tanggal_buat = models.DateField(auto_now_add=True, null=True)
	tanggal_pinjam = models.DateField(null=True)
	tanggal_kembali = models.DateField(null=True)
	buku = models.ForeignKey(Buku, on_delete=models.CASCADE, null=False)
	peminjam = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
	status = models.ForeignKey(StatusTransaksi, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.tanggal_buat.strftime("%d/%b/%Y")