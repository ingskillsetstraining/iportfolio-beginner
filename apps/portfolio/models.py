# apps/portfolio/models.py

from django.db import models

class KontenHalaman(models.Model):
    judul = models.CharField(max_length=200)
    sub_judul = models.TextField()

    # Kelas konfigurasi tambahan khusus untuk mengatur tampilan nama tabel di admin panel
    class Meta:
        # Mengatur nama kustom agar terbebas dari aturan tambahan huruf 's' otomatis
        verbose_name_plural = "Konten Halaman"

    # Fungsi khusus Python untuk mengubah objek mentah menjadi teks yang mudah dibaca manusia
    def __str__(self):
        # Memerintahkan Django untuk selalu mencetak isi dari kolom judul data tersebut
        return self.judul
