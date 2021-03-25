from django.urls import path
from .views import *

urlpatterns = [
	path('buku/', ListBuku.as_view(), name="apiBuku"),
	path('buku/<int:pk>', DetailBuku.as_view(), name="apiDetailBuku"),

	path('user/', ListUser.as_view(), name="apiUser"),
	path('user/<int:pk>', DetailUser.as_view()),

	path('trans/', ListTrans.as_view(), name="apiTrans"),
	path('trans/<int:pk>', DetailTrans.as_view()),

]