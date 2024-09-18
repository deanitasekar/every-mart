# Every Mart
### <b>🛒 Toko Online Serba Ada untuk Semua Kebutuhan Anda 🛒</b>
###### Nama: Deanita Sekar Kinasih
###### NPM: 2306229405
###### Kelas: PBP-D
###### Link: http://deanita-sekar-everymart.pbp.cs.ui.ac.id/

## Tugas 3: Implementasi Form dan Data Delivery pada Django
### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?


### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
● Mengubah primary key dari integer menjadi UUID untuk best practice dari sisi keamanan aplikasi dengan melakukan modifikasi 'models.py'
```py
import uuid # modifikasi
from django.db import models

class Product(models.Model) :
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # modifikasi
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
```
● Melakukan migrasi model melalui terminal
```
python manage.py makemigrations
python manage.py migrate
```
● Membuat 'forms.py' dalam 'main' untuk menerima Product Entry Form baru
```py
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock"]
```
● Melakukan modifikasi dengan menambahkan import pada 'views.py' dalam 'main'
```py
from django.shortcuts import render, redirect
```
● Melakukan modifikasi pada 'views.py' dalam 'main' dengan menambahkan fungsi 'create_product' untuk menghasilkan form yang dapat menambahkan Product Entry secara otomatis
```py
def create_product(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```
● Melakukan modifikasi pada 'views.py' dalam 'main' dengan mengubah fungsi 'show_main'
```py
def show_main(request):
    products = Product.objects.all()
    context = {
        'npm' : '2306229405',
        'name': 'Deanita Sekar Kinasih',
        'class': 'PBP D',
        'products' : products,
    }

    return render(request, "main.html", context)
```
● Melakukan modifikasi pada 'urls.py' dalam 'main' dengan menambahkan import dan menambahkan path URL
```py
from main.views import show_main
```
```py
    path('create-product', create_product, name='create_product'),
```
● Membuat 'create_product.html' dalam 'main/templates'
```py
{% extends 'base.html' %} 
{% block content %}
<h1>Add Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
● Menjalankan proyek Django melalui terminal untuk mengecek fungsionalitas
```
python manage.py runserver
```
● Melakukan modifikasi 'main.html' dalam 'main/templates' untuk menampilkan data dalam bentuk table serta tombol 'Add Product'
```py
{% if not products %}
<p>Belum ada product yang terdaftar!</p>
{% else %}
<table>
  <tr>
    <th>Name</th>
    <th>Price</th>
    <th>Description</th>
    <th>Stock</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data product di bawah baris ini 
  {% endcomment %} 
  {% for product in products %}
  <tr>
    <td>{{product.name}}</td>
    <td>{{product.price}}</td>
    <td>{{product.description}}</td>
    <td>{{product.stock}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product' %}">
  <button>Add New Product</button>
</a>
```
● Melakukan modifikasi pada 'views.py' dalam 'main' dengan menambahkan import dan menambahkan fungsi 'show_xml' untuk mengembalikan data dalam bentuk XML
``` py
from django.http import HttpResponse
from django.core import serializers
```
``` py
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
● Melakukan modifikasi pada 'urls.py' dalam 'main' dengan menambahkan import dan menambahkan path URL
```py
from main.views import show_main, create_mood_entry, show_xml
```
```py
    path('xml/', show_xml, name='show_xml'),
```
● Melakukan modifikasi pada 'views.py' dalam 'main' dengan menambahkan fungsi 'show_json' untuk mengembalikan data dalam bentuk JSON
```py
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
● Melakukan modifikasi pada 'urls.py' dalam 'main' dengan menambahkan import dan menambahkan path URL
```py
from main.views import show_main, create_mood_entry, show_xml, show_json
```
```py
    path('json/', show_json, name='show_json'),
```
● Melakukan modifikasi pada 'views.py' dalam 'main' dengan menambahkan fungsi 'show_xml_by_id' dan 'show_json_by_id' untuk menerima parameter 'request' dan 'id' untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON
```py
def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
● Melakukan modifikasi pada 'urls.py' dalam 'main' dengan menambahkan import dan menambahkan path URL
```py
from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
```
```py
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```
● Menjalankan proyek Django melalui terminal untuk mengecek fungsionalitas dan menggunakan Postman sebagai Data Viewer
```
python manage.py runserver
```

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman

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
```py
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
```py
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
```py
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
```py
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
● Mengonfigurasi routing URL proyek dengan melakukan modifikasi urls.py dalam direktore'every_mart'
```py
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
```py
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
###### Bagan
![Bagan](/diagram.png)
###### Alur
- Client dapat melaukan request, Internet akan melanjutkan HTTP request dan urls akan melanjutkan Route Request. views akan melanjutkan ke models dan template
- views melakukan display data ke template dan template mengembalikan data input ke views
- views akan melakukan modifikasi data ke models dan models akan mengakses database untuk melakukan modifikasi. Request akan dikembalikan ke models dan data akan dikembalikan ke views
- views melakukan display data ke template dan template mengembalikan data input ke views
- Setelah semua Request terpenuhi, views akan mengembalikan ke Internet dan Internet akan mengembalikan ke Client dalam bentuk Web Page
###### Keterkaitan antara urls.py, views.py, models.py, dan berkas html
'urls.py' berfungsi sebagai peta dalam web aplikasi dan menghubungkan pola URL sesuai dengan 'views.py'. 'views.py' menangani HTTP Request dan mengembalikan respons, serta berinteraksi dengan 'models.py' untuk memodifikasi data. 'models.py' akan menyediakan abstraksi untuk interaksi dengan database. 'berkas html' akan menentukan bagaimana data dari 'views.py' ditampilkan kepada Client

### Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah alat software development yang memiliki fungsi sebagai version control system untuk melacak dan mengelola source code secara efisien. Dalam pengembangan perangkat lunak, Git memiliki beberapa peranan penting, yaitu:
- Git membantu pelacakan perubahan kode dengan informasi lengkap tentang apa yang diubah, siapa yang melakukan perubaham, dan kapan dilakukan perubahan
- Git memudahkan dalam melakukan branching karena dapat membuat branch baru untuk keperluan pengembangan perangkat lunak dan branch tersebut dapat di-merge apabila diperlukan
- Git menyimpan riwayat perubahan kode pada setiap commit yang dilakukan sehingga dimungkinkan untuk kembali ke versi sebelumnya apabila diperlukan
- Git menyediakan berbagai fitur yang dapat memudahkan kolaborasi dalam waktu yang bersamaan untuk mempermudah pengembangan perangkat lunak dengan banyak developer

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django sebagai permulaan pembelajaran pengembangan perangkat lunak menawarkan kombinasi unik yang jarang ditemui pada framework lain. Penggunaan bahasa pemrograman Python memberi kemudahan karena sintaksnya bersih sehingga developer dapat mempelajari pengembangan perangkat lunak tanpa terjebak dalam sintaks yang rumit. 
Framework Django memiliki arsitektur MVT (Model-View-Template) menghadirkan struktur yang logis dan intuitif untuk memahami alur pengembangan perangkat lunak. Selain itu, adanya ORM (Object-Relational Mapping) dapat membuat interaksi dengan database menjadi lebih mudah karena developer tidak perlu menulis kode SQL secara langsung. Tidak terbatas di situ saja, framework ini memiliki keunggulan dengan keamanan yang terintegrasi secara default. 
Berdasarkan pengamatan saya selama beberapa minggu perkuliahan PBP, saya meyakini bahwa framework Django dapat menjadi framework yang paling cocok untuk memulai pembelajaran dalam pengembangan perangkat lunak dan memiliki potensi besar untuk pengembangan perangkat lunak lanjutan. 

### Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena perannya sebagai jembatan penghubung antara objek dalam Python dengan database relasional. ORM Django memungkinkan developer untuk mendefinisikan struktur data dan relasi menggunakan Python yang secara otomatis diterjemahkan ke dalam skema database dan operasi SQL yang sesuai. Mekanisme ini memudahkan developer untuk berinteraksi dengan databse menggunakan Python tanpa perlu menulis query SQL kompleks secara langsung. ORM yang dimiliki oleh Django membantu developer untuk berfokus pada pengembangan perangkat lunak daripada implementasi database.
