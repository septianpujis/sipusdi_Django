from import_export import resources
from import_export.fields import Field
from transaksi.models import *
from user.models import *
from buku.models import *

class Resource(resources.ModelResource):
	id_trans = Field(attribute='id', column_name='Id Transaksi')
	tanggal_buat = Field(attribute='tanggal_buat', column_name='Tanggal Transaksi Dibuat')
	tanggal_pinjam = Field(attribute='tanggal_pinjam', column_name='Tanggal Buku Dipinjam')
	tanggal_kembali = Field(attribute='tanggal_kembali', column_name='Tanggal Dikembalikan')
	peminjam__nama = Field(attribute='peminjam__nama', column_name='Nama Peminjam')
	buku__judul = Field(attribute='buku__judul', column_name='Judul Buku')
	status__nama = Field(attribute='status__nama', column_name='Status Transaksi')
	class Meta:
		model = Transaksi
		fields = ['tanggal_buat','tanggal_pinjam','tanggal_kembali','peminjam__nama','buku__judul','status__nama']