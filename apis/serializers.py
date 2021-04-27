from rest_framework import serializers
from buku import models
from user import models
from transaksi import models

class BukuSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = models.Buku

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ['id','nama','email', 'no_telp']
		model = models.User

class TransSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = models.Transaksi
