from django.urls import path
from . import views

urlpatterns = [
   path('dashboard/',views.dashboard,name='dashboard'),
   path('profile/',views.profile,name='manage_profile'),
   path('matakuliah/',views.matakuliah,name='manage_matakuliah'),
   path('mahasiswa/',views.mahasiswa,name='manage_mahasiswa'),
   path('dosen/',views.dosen,name='manage_dosen'),
   path('hubungikami/',views.hubungikami,name='manage_hubungikami'),
   path('jurusan/',views.jurusan,name='manage_jurusan'),
   path('tambah_jurusan/',views.tambah_jurusan,name='manage_tambah_jurusan'),
   path('edit_jurusan/<int:jurusanid>/',views.edit_jurusan,name='edit_jurusan'),
   path('hapus_jurusan/<int:jurusanid>/',views.hapus_jurusan,name='hapus_jurusan'),
   path('mahasiswa/',views.mahasiswa,name='manage_mahasiswa'),
   path('tambah_mahasiswa/',views.tambah_mahasiswa,name='manage_tambah_mahasiswa'),
   path('edit_mahasiswa/<int:mhsid>/',views.edit_mahasiswa,name='edit_mahasiswa'),
   path('hapus_mahasiswa/<int:mhsid>/',views.hapus_mahasiswa,name='hapus_mahasiswa'),
   path('tambah_dosen/',views.tambah_dosen,name='manage_tambah_dosen'),
   path('view-dosen/<int:dosenid>/',views.viewdosen,name='view_dosen'),

   
   
   
 

    
]
