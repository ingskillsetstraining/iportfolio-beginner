# config/urls.py

from django.contrib import admin
from django.urls import path
from portfolio.views import portfolio_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_home),
]