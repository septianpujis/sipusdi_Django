from django.shortcuts import render, redirect
from buku.models import *
from buku.form import FormBuku
from django.conf import settings
from django.contrib import messages

# Create your views here.

def index(request):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		data_buku = Buku.objects.all()
		
		var ={
			'buku' : data_buku,
			'judul' : "Data Buku",
		}
		return render(request, 'tampilBuku.html', var)


def tambah(request):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.session['level']==1:
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
		else:
			messages.warning(request, 'Gagal menambah data, Bukan Admin')
			return redirect('tampilBuku')

def edit(request, id_buku):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.session['level']==1:
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
		else:
			messages.warning(request, 'Gagal menyunting data, Bukan Admin')
			return redirect('tampilBuku')

def hapus(request, id_buku):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.session['level']==1:
			data = Buku.objects.filter(id=id_buku)
			data.delete()
			messages.success(request, 'Data Berhasil Dihapus')
			return redirect('tampilBuku')
		else:
			messages.warning(request, 'Gagal menghapus data, Bukan Admin')
			return redirect('tampilBuku')