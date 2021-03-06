from django.db import models

# Create your models here.

class Genre(models.Model):
	nama = models.CharField(max_length=20)
	keterangan = models.CharField(max_length=70)
	
	def __str__(self):
		return self.nama

class Buku(models.Model):
	judul = models.CharField(max_length=80)
	penulis = models.CharField(max_length=80)
	penerbit = models.CharField(max_length=80)
	tahun = models.IntegerField(null=True)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
	sinopsis = models.CharField(max_length=300)
	cover = models.ImageField(upload_to='cover/',null=True)
	tanggal = models.DateField(auto_now_add=True, null=True)

	def __str__(self):
		return self.judul
