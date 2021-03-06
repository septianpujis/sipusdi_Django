from django.contrib import admin
from user.models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ['id','nama','level','password','email']
	search_fields = ['nama', 'id']
	#list_filter = ('kelompok_id',)



admin.site.register(Level)
admin.site.register(User, UserAdmin)
admin.site.register(KodeKelas)