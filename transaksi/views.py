from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	var ={
		'judul' : "Data Peminjaman",
	}
	return render(request, 'tampilTrans.html', var)


def tambah(request):
	var ={
		'judul' : "Tambah Data Peminjaman",
	}
	return render(request, 'tambahTrans.html', var)


def edit(request, id_trans):
	var ={
		'judul' : "Sunting Data Peminjaman",
	}
	return render(request, 'editTrans.html', var)


def hapus(request, id_trans):
	var ={
		'id_trans':id_trans,
		'judul' : "Hapus Data Peminjaman",
	}
	return redirect('tampilTrans')