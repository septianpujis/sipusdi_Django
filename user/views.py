from django.shortcuts import render, redirect
from user.models import *
from user.form import FormUser
from django.conf import settings
from django.contrib import messages
# Create your views here.

def index(request):	
	var ={
		'user' : User.objects.all(),
		'judul' : "Data user",
	}
	return render(request, 'tampilUser.html', var)


def tambah(request):
	if request.POST:
		form = FormUser(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Data Berhasil Ditambahkan')
			return redirect('tampilUser')
	else:
		form = FormUser()
		var ={
			'form':form,
			'judul' : "Tambah Data Pengguna",
		}
		return render(request, 'tambahUser.html', var)


def edit(request, id_user):
	user = User.objects.get(id=id_user)
	if request.POST:
		form = FormUser(request.POST, instance=user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Data Berhasil Diubah')
			return redirect('tampilUser')
	else:
		form = FormUser(instance=user)
		var ={
		'form':form,
		'judul' : "Sunting Data User",
		'user':user,
		}
		return render(request, 'editUser.html', var)


def hapus(request, id_user):
	data = User.objects.filter(id=id_user)
	data.delete()
	messages.success(request, 'Data Berhasil Dihapus')

	return redirect('tampilUser')