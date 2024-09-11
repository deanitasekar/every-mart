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

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
<b> Alur </b>
- Client dapat melaukan request, Internet akan melanjutkan HTTP request dan urls akan melanjutkan Route Request. views akan melanjutkan ke models dan template
- views melakukan display data ke template dan template mengembalikan data input ke views
- views akan melakukan modifikasi data ke models dan models akan mengakses database untuk melakukan modifikasi. Request akan dikembalikan ke models dan data akan dikembalikan ke views
- views melakukan display data ke template dan template mengembalikan data input ke views
- Setelah semua Request terpenuhi, views akan mengembalikan ke Internet dan Internet akan mengembalikan ke Client dalam bentuk Web Page
<b> Keterkaitan antara urls.py, views.py, models.py, dan berkas html </b>
'urls.py' bergungsi sebagai peta dalam web aplikasi dan menghubungkan pola URL sesuai dengan 'views.py'. 'views.py' menganai HTTP Request dan mengembalikan respons, serta berinteraksi dengan 'models.py' untuk memodifikasi data. 'models.py' akan menyediakan abstraksi untuk interaksi dengan database. 'berkas html' akan menentukan bagaimana data dari 'views.py' ditampilkan kepada Client

### Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah alat software development yang memiliki fungsi sebagai version control sistem untuk melacak dan mengelola source code secara efisien. Dalam pengembangan perangkat lunak, Git memiliki beberapa peranan penting, yaitu:
- Git membantu melacak perubahan kode dengan informasi lengkap tentang apa yang diubah, siapa yang melakukan perubaham, dan kapan dilakukan perubahan
- Git memudahkan dalam melakukan branching karena dapat membuat branch baru untuk keperluan pengembangan perangkat lunak dan branch tersebut dapat di-merge apabila diperlukan
- Git menyimpan riwayat perubahan kode pada setiap commit yang dilakukan sehingga dimungkinkan untuk kembali ke versi sebelumnya apabila diperlukan
- Git menyediakan berbagai fitur yang dapat memudahkan kolaborasi antar developer dalam waktu yang bersamaan untuk mempermudah pengembangan perangkat lunak dengan banyak developer

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django sebagai permulaan pembelajaran pengembangan perangkat lunak menawarkan kombinasi unik yang jarang ditemui pada framework lain. Penggunaan bahasa pemrograman Python memberi kemudahan karena sintaksnya bersih sehingga developer dapat mempelajari pengembangan perangkat lunak tanpa terjebak dalam sintaks yang rumit. 
Framework Django memiliki arsitektur MVT (Model-View-Template) menghadirkan struktur yang logis dan intuitif untuk memahami alur pengembangan perangkat lunak. Selain itu, adanya ORM (Object-Relational Mapping) dapat membuat interaksi dengan database menjadi lebih mudah karena developer tidak perlu menulis kode SQL secara langsung. Tidak terbatas di situ saja, framework ini memiliki keunggulan dengan keamanan yang terintegrasi secara default. 
Berdasarkan pengamatan saya selama beberapa minggu perkuliahan PBP, saya meyakini bahwa framework dapat menjadi framework yang paling cocok untuk memulai pembelajaran dalam pengembangan perangkat lunak dan memiliki potensi besar untuk pengembangan perangkat lunak lanjutan. 

### Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena perannya sebagai jembatan penghubung antara objek dalam Python dengan database relasional. ORM Django memungkinkan developer untuk mendefinisikan struktur data dan relasi menggunakan Python yang secara otomatis diterjemahkan ke dalam skema database dan operasi SQL yang sesuai. Mekanisme ini memudahkan developer untuk berinteraksi dengan databse menggunakan Python tanpa perlu menulis query SQL kompleks secara langsung. ORM yang dimiliki oleh Django membantu developer untuk berfokus pada pengembangan perangkat lunak daripada implementasi databse. 
