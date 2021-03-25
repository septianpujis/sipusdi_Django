from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from buku import models
from user import models
from transaksi import models
from .serializers import *

class ListBuku(generics.ListCreateAPIView):
	queryset = models.Buku.objects.all()
	serializer_class = BukuSerializer

class DetailBuku(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Buku.objects.all()
	serializer_class = BukuSerializer

class ListUser(generics.ListCreateAPIView):
	queryset = models.User.objects.all()
	serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.User.objects.all()
	serializer_class = UserSerializer

class ListTrans(generics.ListCreateAPIView):
	queryset = models.Transaksi.objects.all()
	serializer_class = TransSerializer

class DetailTrans(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Transaksi.objects.all()
	serializer_class = TransSerializer
# Create your views here.
