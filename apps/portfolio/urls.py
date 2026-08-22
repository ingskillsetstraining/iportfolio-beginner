# apps/portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Mengarahkan rute utama aplikasi ke fungsi view bernama home
    path('', views.home, name='home'),
]