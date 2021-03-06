from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	var ={
		'judul' : "Data Pengguna",
	}
	return render(request, 'tampilUser.html', var)


def tambah(request):
	var ={
		'judul' : "Tambah Data Pengguna",
	}
	return render(request, 'tambahUser.html', var)


def edit(request, id_user):
	var ={
		'judul' : "Sunting Data Pengguna",
	}
	return render(request, 'editUser.html', var)


def hapus(request, id_user):
	var ={
		'user_id': id_user,
		'judul' : "Hapus Data Pengguna",
	}
	return redirect('tampilUser')