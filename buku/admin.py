from django.contrib import admin
from buku.models import *

# Register your models here.

class BukuAdmin(admin.ModelAdmin):
	list_display = ['cover', 'id','judul','penulis','penerbit','tahun']
	search_fields = ['judul','penulis','penerbit']
	#list_filter = ('kelompok_id',)



admin.site.register(Genre)
admin.site.register(Buku, BukuAdmin)