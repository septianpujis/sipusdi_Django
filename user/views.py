from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import *
from user.form import FormUser
from django.conf import settings
from django.contrib import messages
from user.resource import Resource
# Create your views here.

def index(request):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		data_user = User.objects.all()
		var ={
			'user' : data_user,
			'judul' : "Data Pengguna",
		}
		return render(request, 'tampilUser.html', var)


def tambah(request):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.session['level']==1:
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
		else:
			messages.warning(request, 'Gagal menambah data, Bukan Admin')
			return redirect('tampilUser')


def edit(request, id_user):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.session['level']==1:
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
				'judul' : "Sunting Data Pengguna",
				'user':user,
				}
				return render(request, 'editUser.html', var)
		else:
			messages.warning(request, 'Gagal menyunting data, Bukan Admin')
			return redirect('tampilUser')


def hapus(request, id_user):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.session['level']==1:
			data = User.objects.filter(id=id_user)
			data.delete()
			messages.success(request, 'Data Berhasil Dihapus')

			return redirect('tampilUser')
		else:
			messages.warning(request, 'Gagal menghapus data, Bukan Admin')
			return redirect('tampilUser')


def laporan(request):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.session['level']==1:
			data = Resource()
			dataset = data.export()
			response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
			response['Content-Disposition'] = 'attachment; filename=Laporan-User.xls'
			return response
		else:
			messages.warning(request, 'Gagal Mengeksport data, Bukan Admin')
			return redirect('tampilUser')
