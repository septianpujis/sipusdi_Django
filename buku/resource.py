from import_export import resources
from import_export.fields import Field
from buku.models import *

class Resource(resources.ModelResource):
	judul = Field(attribute='judul', column_name='Judul Buku')
	penulis = Field(attribute='penulis', column_name='Penulis')
	penerbit = Field(attribute='penerbit', column_name='Penerbit')
	tahun = Field(attribute='tahun', column_name='Tahun Terbit')
	genre__nama = Field(attribute='genre__nama', column_name='Genre Buku')

	class Meta:
		model = Buku
		fields =['judul','penulis','penerbit','tahun','genre__nama']

