"""sipusdi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sipusdi import views as base
from buku import views as buku
from user import views as user
from transaksi import views as transaksi
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base.index, name='index' ),
    path('login/', base.login, name='login' ),
    path('logout/', base.logout, name='logout' ),

    path('buku/', buku.index , name='tampilBuku' ),
    path('buku/tambah/', buku.tambah, name='tambahBuku' ),
    path('buku/edit/<int:id_buku>', buku.edit, name='editBuku' ),
    path('buku/hapus/<int:id_buku>', buku.hapus, name='hapusBuku' ),

    path('user/', user.index, name='tampilUser' ),
    path('user/tambah/', user.tambah, name='tambahUser' ),
    path('user/edit/<int:id_user>', user.edit, name='editUser' ),
    path('user/hapus/<int:id_user>', user.hapus, name='hapusUser' ),

    path('transaksi/', transaksi.index, name='tampilTrans' ),
    path('transaksi/tambah/', transaksi.tambah, name='tambahTrans' ),
    path('transaksi/edit/<int:id_trans>', transaksi.edit, name='editTrans' ),
    path('transaksi/hapus/<int:id_trans>', transaksi.hapus, name='hapusTrans' ),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
