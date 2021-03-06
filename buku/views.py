from django.shortcuts import render, redirect
from buku.models import *
from buku.form import FormBuku
from django.conf import settings
from django.contrib import messages

# Create your views here.

def index(request):
	data_buku = Buku.objects.all()
	
	var ={
		'buku' : data_buku,
		'judul' : "Data Buku",
	}
	return render(request, 'tampilBuku.html', var)


def tambah(request):
	if request.POST:
		form = FormBuku(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Data Berhasil Ditambahkan')
			return redirect('tampilBuku')
	else:
		form = FormBuku()
		var ={
			'form':form,
			'judul' : "Tambah Data Buku",
		}
		return render(request, 'tambahBuku.html', var)


def edit(request, id_buku):
	buku = Buku.objects.get(id=id_buku)
	if request.POST:
		form = FormBuku(request.POST, request.FILES, instance=buku)
		if form.is_valid():
			form.save()
			messages.success(request, 'Data Berhasil Diubah')
			return redirect('tampilBuku')
	else:
		form = FormBuku(instance=buku)
		var ={
		'form':form,
		'judul' : "Sunting Data Buku",
		'buku':buku,
		}
		return render(request, 'editBuku.html', var)


def hapus(request, id_buku):
	buku = Buku.objects.filter(id=id_buku)
	buku.delete()
	messages.success(request, 'Data Berhasil Dihapus')

	return redirect('tampilBuku')