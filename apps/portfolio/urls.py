# apps/portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Mengarahkan rute utama aplikasi ke fungsi view bernama home
    path('', views.home, name='home'),
    
    # Menambahkan rute alamat untuk halaman about
    path('about/', views.about, name='about'),
    
    # Menambahkan rute alamat untuk halaman portfolio
    path('portfolio/', views.portfolio, name='portfolio'),
    
    # Menambahkan rute alamat untuk halaman services
    path('services/', views.services, name='services'),
    
    # Menambahkan rute alamat untuk halaman skills
    path('skills/', views.skills, name='skills'),
    
    # Menambahkan rute alamat untuk halaman testimoni
    path('testimoni/', views.testimoni, name='testimoni'),
]