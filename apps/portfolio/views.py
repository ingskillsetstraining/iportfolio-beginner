# apps/portfolio/views.py

# Modul Django bawaan untuk merender template HTML (belum kita gunakan sekarang)
from django.shortcuts import render

# Modul Django khusus untuk mengirimkan respon teks biasa ke browser internet
from django.http import HttpResponse

# Fungsi View contoh untuk menyapa pengunjung pertama kali
def halo_dunia(request):
    # Setiap fungsi View WAJIB menerima satu argumen 'request' yang berisi data kiriman dari browser
    
    # Fungsi ini mengembalikan respon teks instan ke layar browser pengunjung
    return HttpResponse("Halo Dunia!")
