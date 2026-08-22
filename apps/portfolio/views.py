# apps/portfolio/views.py

from django.shortcuts import render

def portfolio_home(request):
    # Mengarahkan rute ke dalam sub-folder portfolio
    return render(request, 'portfolio/index.html')
