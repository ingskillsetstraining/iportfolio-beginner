# apps/portfolio/views.py

from django.shortcuts import render

def home(request):
    # Memerintahkan Django untuk mencari dan menampilkan berkas desain bernama home.html
    return render(request, 'portfolio/home.html')# apps/portfolio/views.py

# Fungsi view baru khusus untuk halaman About
def about(request):
    # Memerintahkan Django untuk mencari dan merender file about.html
    return render(request, 'portfolio/about.html')
