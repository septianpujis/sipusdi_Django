from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	var ={
		'judul' : "Data Buku",
	}
	return render(request, 'tampilBuku.html', var)


def tambah(request):
	var ={
		'judul' : "Tambah Data Buku",
	}
	return render(request, 'tambahBuku.html', var)


def edit(request, id):
	var ={
		'judul' : "Sunting Data Buku",
	}
	return render(request, 'editBuku.html', var)


def hapus(request, id):
	var ={
		'judul' : "Hapus Data Buku",
	}
	return redirect('tampilBuku.html', var)