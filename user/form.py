from django.forms import ModelForm
from django import forms
from user.models import User

class FormUser(ModelForm):
	class Meta:
		model = User
		fields = '__all__'
		#fields = ['judul','penulis']
		#exclude = ['penulis']

		widgets ={
			'nis' : forms.NumberInput({'class':'form-control', 'min':'1'}),
			'nama' : forms.TextInput({'class':'form-control'}),
			'level' : forms.Select({'class':'form-control'}),
			'password' : forms.PasswordInput({'class':'form-control'}),
			'kelas' : forms.Select({'class':'form-control'}),
			'email' : forms.EmailInput({'class':'form-control'}),
			'no_telp' : forms.NumberInput({'class':'form-control', 'minlength':'10'}),
		}