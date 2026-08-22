# apps/portfolio/views.py

from django.shortcuts import render

def portfolio_home(request):
    # Membuat wadah kamus data (dictionary) bernama context
    context = {
        'judul': 'Selamat Datang di iPortfolio!',
        'sub_judul': 'Halaman ini dipanggil menggunakan struktur templates global.',
    }
    
    # Mengirimkan wadah context sebagai argumen ketiga di dalam fungsi render
    return render(request, 'portfolio/index.html', context)
