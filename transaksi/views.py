from django.http import HttpResponse
from django.shortcuts import render, redirect
from transaksi.models import *
from transaksi.form import FormTrans
from django.conf import settings
from django.contrib import messages
from transaksi.resource import Resource

# Create your views here.

def index(request):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.GET:
			data_trans = Transaksi.objects.filter(tanggal_pinjam=request.GET.get('query', ''))
		else:
			data_trans = Transaksi.objects.all()

		var ={
			'trans' : data_trans,
			'judul' : "Data Peminjaman",
		}
		return render(request, 'tampilTrans.html', var)


def tambah(request):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.POST:
			form = FormTrans(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, 'Data Berhasil Ditambahkan')
				return redirect('tampilTrans')
		else:
			form = FormTrans()
			var ={
				'form':form,
				'judul' : "Tambah Data Peminjaman",
			}
			return render(request, 'tambahTrans.html', var)


def edit(request, id_trans):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.session['level']==1:
			trans = Transaksi.objects.get(id=id_trans)
			if request.POST:
				form = FormTrans(request.POST, instance=trans)
				if form.is_valid():
					form.save()
					messages.success(request, 'Data Berhasil Diubah')
					return redirect('tampilTrans')
			else:
				form = FormTrans(instance=trans)
				var ={
				'form':form,
				'judul' : "Sunting Data Peminjaman",
				'trans':trans,
				}
				return render(request, 'editTrans.html', var)
		else:
			messages.warning(request, 'Gagal menyunting data, Bukan Admin')
			return redirect('tampilTrans')


def hapus(request, id_trans):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		if request.session['level']==1:
			data = Trans.objects.filter(id=id_trans)
			data.delete()
			messages.success(request, 'Data Berhasil Dihapus')
			return redirect('tampilTrans')
		else:
			messages.warning(request, 'Gagal menghapus data, Bukan Admin')
			return redirect('tampilTrans')


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
			response['Content-Disposition'] = 'attachment; filename=Laporan-Transaksi.xls'
			return response
		else:
			messages.warning(request, 'Gagal Mengeksport data, Bukan Admin')
			return redirect('tampilTrans')