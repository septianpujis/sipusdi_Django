from django.shortcuts import render
from rest_framework import generics
from buku import models
from .serializers import *

class ListBuku(generics.ListCreateAPIView):
	queryset = models.Buku.objects.all()
	serializer_class = BukuSerializer

class DetailBuku(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Buku.objects.all()
	serializer_class = BukuSerializer

# Create your views here.
