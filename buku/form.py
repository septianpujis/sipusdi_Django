from django.forms import ModelForm
from django import forms
from buku.models import Buku

class FormBuku(ModelForm):
	class Meta:
		model = Buku
		fields = '__all__'
		#fields = ['judul','penulis']
		#exclude = ['penulis']

		widgets ={
			'judul' : forms.TextInput({'class':'form-control'}),
			'penulis' : forms.TextInput({'class':'form-control'}),
			'penerbit' : forms.TextInput({'class':'form-control'}),
			'tahun' : forms.NumberInput({'class':'form-control', 'min':'1940', 'max':'4000'}),
			'genre' : forms.Select({'class':'form-control'}),
			'sinopsis' : forms.TextInput({'class':'form-control'}),
		}