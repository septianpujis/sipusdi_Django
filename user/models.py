from django.db import models

# Create your models here.
class KodeKelas(models.Model):
	nama = models.CharField(max_length=20)
	def __str__(self):
		return self.nama

class Level(models.Model):
	nama = models.CharField(max_length=20)
	def __str__(self):
		return self.nama

class User(models.Model):
	nis = models.IntegerField(null=False)
	nama = models.CharField(max_length=40)
	level = models.ForeignKey(Level, on_delete=models.CASCADE, null=False)
	password = models.CharField(max_length=20)
	kelas = models.ForeignKey(KodeKelas, on_delete=models.CASCADE, null=False)
	email = models.CharField(max_length=50)
	no_telp = models.CharField(max_length=20)