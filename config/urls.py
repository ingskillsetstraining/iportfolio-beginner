# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Menghubungkan dan memasukkan seluruh rute alamat dari file portfolio.urls
    path('', include('portfolio.urls')),
]