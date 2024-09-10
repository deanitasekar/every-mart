# Every Mart
### <b>🛒 Toko Online Serba Ada untuk Semua Kebutuhan Anda 🛒</b>
###### Deanita Sekar Kinasih | 2306229405 | PBP-D
##### http://deanita-sekar-everymart.pbp.cs.ui.ac.id/

## Tugas 2: Implementasi Model-View-Template (MVT) pada Django
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
● Membuat direktori lokal bernama 'every-mart' dan masuk ke direktori tersebut melalui terminal
```
cd <path_direktori>\every-mart
```
● Melakukan konfigurasi nama pengguna dan alamat email agar terhubung dengan Git

```
git config --global user.name "<NAME>"
git config --global user.email "<EMAIL>"
```
● Membuat repositori GitHub dengan nama 'every-mart' dan menghubungkan dengan direktori lokal
```
git branch -M main
git remote add origin https://github.com/deanitasekar/every-mart.git
```
● Memulai instalasi Django dengan mengaktifkan virtual environment
```
python -m venv env
env\Scripts\activate
```
● Menyiapkan dependencies dengan membuat berkas 'requirements.txt' dan melakukan instalansi dependencies
```
pip install -r requirements.txt
```
● Membuat proyek Django bernama 'every_mart'
```
django-admin startproject every_mart .
```
● Melakukan modifikasi pada 'ALLOWED_HOTS' di 'settings.py' untuk deployment dan menjalankan server Django
```
python manage.py runserver
```
● Membuat aplikasi bernama 'main' dalam proyek dan melakukan modifikasi pada 'INSTALLED_APPS' di 'settings.py' dalam direktori
```
python manage.py startapp main
```
● Membuat 'main.html' dan mengisi sesuai dengan kode yang diharapkan
```
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Every Mart - Toko Online Serba Ada</title>
</head>
<body>

<body>
    <h2>Welcome to Every Mart!</h2>
    <p>🛒 Toko Online Serba Ada untuk Semua Kebutuhan Anda 🛒</p>

    <h4>Halo, {{ name }} dengan NPM {{ npm }} dari kelas {{ class }} 👋</h4>
    <p>Mulai perjalananmu bersama Every Mart sekarang!</p> 
</body>
</html>
```
● Melakukan modifikasi 'models.py' dalam direktori aplikasi 'main'
```
from django.db import models

class Product(models.Model) :
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
```
● Melakukan migrasi model untuk mengaplikasikan models ke dalam basis data
```
python manage.py makemigrations
python manage.py migrate
```
● Mengintegrasikan komoponen MVT dengan melakukan modifikasi 'views.py' dalam direktori aplikasi 'main'
```
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306229405',
        'name': 'Deanita Sekar Kinasih',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
```
● Mengonfigurasi routing URL aplikasi 'main' dengan membuat berkas 'urls.py'
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
● Mengonfigurasi routing URL proyek dengan melakukan modifikasi urls.py dalam direktore'every_mart'
```
...
from django.urls import path, include
...

urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```
● Mencoba proyek Django secara lokal
```
python manage.py runserver
```
● Menambahkan berkas '.gitignore' dan mengunggah proyek ke repositori Github 'every-mart'
```
git add .
git commit -m "..."
git push origin main
```
● Mengakses halaman PWS pada https://pbp.cs.ui.ac.id.dan membuat proyek baru dengan nama 'everymart'
● Melakukan modifikasi 'settings.py' pada 'ALLOWED_HOSTS' untuk menghubungkan dengan URL deplotment PWS
```
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "deanita-sekar-everymart.pbp.cs.ui.ac.id"]
```
● Mengunggah perubahan pada repositori GituHub dan melakukan push ke PWS
```
git add .
git commit -m "..."
git push origin main

git branch -M main
git push pws main:master
```
