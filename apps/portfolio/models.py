# apps/portfolio/models.py

from django.db import models

class KontenHalaman(models.Model):
    judul = models.CharField(max_length=200)
    sub_judul = models.TextField()
