from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.form import FormLogin
from user.models import *
from django.contrib import messages

def index(request):
	try:
		request.session['nis']
	except KeyError:
		return redirect('login')
	else:
		var ={
			'judul' : "Halaman Utama",
		}
		return render(request, 'index.html', var)

def login(request):
	if request.POST:
		data = User.objects.filter(nis=request.POST.get("nis"), password=request.POST.get("password")).values()
		# data = User.objects.filter(nis=request.POST.get("nis"), password=request.POST.get("password"))

		if data:
			for row in data:
				request.session.set_expiry(9000)
				request.session['nis'] = row['nis']
				request.session['nama'] = row['nama']
				request.session['no_telp'] = row['no_telp']
				request.session['kelas'] = row['kelas_id']
				request.session['email'] = row['email']
				request.session['level'] = row['level_id']

			return redirect('index')
		else:			
			messages.success(request, 'Password salah')
			var ={
				'form': FormLogin(),
				'judul' : "LOGIN",
			}
			return render(request, 'login.html', var)

		# var={ 'nim': request.POST.get("nis") }
		# return render(request, 'login.html', var)
	else:
		var ={
			'form': FormLogin(),
			'judul' : "LOGIN",
		}
		return render(request, 'login.html', var)

def logout(request):
	request.session.flush()
	return redirect('login')