from import_export import resources
from import_export.fields import Field
from user.models import *

class Resource(resources.ModelResource):
	nis = Field(attribute='nis', column_name='Nomor Induk')
	nama = Field(attribute='nama', column_name='Nama Pengguna')
	kelas__nama = Field(attribute='kelas__nama', column_name='Kelas')
	email = Field(attribute='email', column_name='Email')
	no_telp = Field(attribute='no_telp', column_name='Nomor Telepon')

	class Meta:
		model = User
		fields = ['nis','nama','kelas__nama','email','no_telp']
