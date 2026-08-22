# apps/portfolio/views.py

from django.shortcuts import render

def home(request):
    # Memerintahkan Django untuk mencari dan menampilkan berkas desain bernama home.html
    return render(request, 'portfolio/home.html')# apps/portfolio/views.py

# Fungsi view baru khusus untuk halaman About
def about(request):
    # Memerintahkan Django untuk mencari dan merender file about.html
    return render(request, 'portfolio/about.html')

# Fungsi view baru khusus untuk halaman Portfolio
def portfolio(request):
    # Memerintahkan Django untuk mencari dan merender file portfolio.html
    return render(request, 'portfolio/portfolio.html')

# Fungsi view baru khusus untuk halaman Services
def services(request):
    # Memerintahkan Django untuk mencari dan merender file services.html
    return render(request, 'portfolio/services.html')

# Fungsi view baru khusus untuk halaman Skills
def skills(request):
    # Memerintahkan Django untuk mencari dan merender file skills.html
    return render(request, 'portfolio/skills.html')

# Fungsi view baru khusus untuk halaman Testimoni
def testimoni(request):
    # Memerintahkan Django untuk mencari dan merender file testimoni.html
    return render(request, 'portfolio/testimoni.html')
