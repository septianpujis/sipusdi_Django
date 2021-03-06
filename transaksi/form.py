from django.forms import ModelForm
from django import forms
from transaksi.models import Transaksi

class FormTrans(ModelForm):
	class Meta:
		model = Transaksi
		fields = '__all__'
		#fields = ['judul','penulis']
		#exclude = ['penulis']

		widgets ={
			'tanggal_pinjam' : forms.DateInput({'class':'form-control', 'type':'date'}),
			'tanggal_kembali' : forms.DateInput({'class':'form-control', 'type':'date'}),
			'buku' : forms.Select({'class':'form-control'}),
			'peminjam' : forms.Select({'class':'form-control'}),
			'status' : forms.Select({'class':'form-control'}),
		}