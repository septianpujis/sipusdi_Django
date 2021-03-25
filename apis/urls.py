from django.urls import path
from .views import *

urlpatterns = [
	path('', ListBuku.as_view()),
	path('<int:pk>', DetailBuku.as_view()),
]