# config/urls.py

from django.contrib import admin
from django.urls import path

# Mengimpor fungsi halo_dunia langsung dari file views.py milik aplikasi portfolio
from portfolio.views import halo_dunia

urlpatterns = [
    # Jalur khusus untuk mengakses halaman admin, contoh: http://localhost:8000/admin/
    path('admin/', admin.site.urls),
    
    # Jalur utama (root) website, contoh: http://localhost:8000/
    path('', halo_dunia),
]
