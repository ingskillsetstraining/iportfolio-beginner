# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Mengimpor konfigurasi dari settings.py
from django.conf.urls.static import static # Mengimpor fungsi pembuat jalur aset statis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.portfolio.urls')),
]

# Memastikan jalur aset hanya aktif selama status website masih dalam tahap pengembangan (DEBUG = True)
if settings.DEBUG:
    # Menambahkan rute otomatis untuk membaca file dari folder static Anda
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # Menambahkan rute otomatis untuk membaca file dari folder media Anda
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)