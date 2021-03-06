from django.contrib import admin
from transaksi.models import *

# Register your models here.

class TransAdmin(admin.ModelAdmin):
	list_display = ['id','tanggal_buat','tanggal_pinjam','tanggal_kembali','peminjam','buku','status']
	search_fields = ['id', 'status']
	#list_filter = ('kelompok_id',)

admin.site.register(StatusTransaksi)
admin.site.register(Transaksi, TransAdmin)