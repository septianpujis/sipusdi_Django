from rest_framework import serializers
from buku import models

class BukuSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = models.Buku