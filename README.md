# Every Mart
### <b>🛒 Toko Online Serba Ada untuk Semua Kebutuhan Anda 🛒</b>
**Nama: Deanita Sekar Kinasih** <br>
**NPM: 2306229405**<br>
**Kelas: PBP-D**<br>

###### http://deanita-sekar-everymart.pbp.cs.ui.ac.id/
<hr>

<details>
<summary> <strong> Tugas 6: JavaScript dan AJAX </strong> </summary>

### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Penggunaan JavaScript memiliki beberapa manfaat dalam pengembangan aplikasi web, antara lain:
- Interaktivitas dan pengalaman User <br>
  JavaScript memungkinkan developer menambahkan interaktivitas pada aplikasi web untuk meningkatkan pengalaman pengguna, seperti konten dinamis yang merespons aksi dari User
- Manipulasi DOM <br>
  Dengan JavaScript, struktur dari aplikasi web dapat dimodifikasi secara langsung melalui Document Object Model (DOM) sehingga memungkinkan perubahan secara dinamis tanpa perlu reload halaman utama secara keseluruhan
- Penggunaan framework dan library
  Ekosistem JavaScript memiliki berbagai framework dan library untuk memudahkan pengembangan aplikasi web yang kompleks, seperti React, Angular, dan Vue.

Referensi: [JavaScript and its Role in Web Development](https://medium.com/@dhanushkumarsuresh/introduction-to-javascript-and-its-role-in-web-development-8d920aa7b553)
<hr>


### Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi dari penggunaan `await` ketika menggunakan `fetch()` adalah memastikan bahwa eksekusi kode berikutnya menunggu selesainya proses pengolahan data. `fetch()` merupakan asynchronous method, penggunaan `await` akan menghentikan eksekusi sementara hingga respon dari server diterima sehingga alur eksekusi kode tetap berurutan. <br>
Apabila tidak menggunakan `await`, eksekusi kode akan terus berjalan tanpa menunggu proses `fecth()` selesai. Hal ini dapat menyebabkan masalah karena eksekusi kode akan terus berjalan meskipun respon server belum tersedia, yang dapat menyebabkan error seperti "undefined" atau "unresolved promises". Selain itu, tanpa `await`, promises harus ditangani secara manual dan membuat kode menjadi lebih sulit dibaca dan dipahami. <br>
Dapat disimpulkan bahwa penggunaan `await` ketika menggunakan `fetch()` memastikan urutan eksekusi kode yang tepat, meningkatkan keterbacaan kode, dan mengurangi risiko bug akibat respon server yang belum tersedia.
<hr>

### Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Penggunaan decorator `csrf_exempt` memungkinkan `view` menerima request POST tanpa menyertakan `csrf_token`, yang umumnya diperlukan oleh Django sebagai perlindungan terhadap serangan Cross-Site Request Forgery (CSRF). Decorator `csrf_exempt` biasa digunakan saat menggunakan AJAX, terutama ketika POST request dikirim dari JavaScript, dimana `csrf_token` kerapkali tidak disertakan secara otomatis sehingga request POST tersebut ditolak oleh Django. Oleh karena itu, `csrf_exempt` memungkinkan request POST dari AJAX diterima tanpa adanya validasi `csrf_token`, berguna dalam situasi ketika `csrf_token` tidak tersedia atau sukar untuk disertakan. Namun, penggunaan `csrf_exempt` harus dibatase karena menonaktifkan mekanisme keamanan penting dari Django, berpotensi membuka celah keamanan.
<hr>

### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Terdapat beberapa alasan krusial mengapa pembersihan data input pengguna perlu dilakukan di backend juga, tidak hanya frontend, yaitu:
- Frontend dapat dengan mudah dimanipulasi oleh User sehingga perlu adanya pembersihan data input pengguna di backend untuk keamanan yang lebih kuat
- Backend memastikan hanya data yang sudah tervalidasi sepenuhnya untuk disimpan dalam database, mencegah penyimpanan data yang berbahaya
- Backend memiliki efektivitas tinggi dalam mencegah serangan yang kemungkinan besar lolos dari frontend
- Pembersihan data input pengguna di backend memberikan perlindungan terhadap serangan langsung karena penyerang dapat mengirim serangan ke backend secara langsung
- Pembersihan data input pengguna di backend menjamin bahwa semua data diproses dengan standar keamanan yang sama
- Pembersihan data input pengguna di frontend memiliki keterbatasan dalam menangani jenis data, sedangkan pembersihan data input pengguna di backend dapat menangani berbagai jenis data
<hr>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
**Menambahkan error message saat login User**
- Melakukan modifikasi `views.py` pada `main` dengan mengubah fungsi `login_user`
```py
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
else:
    messages.error(request, "Invalid username or password. Please try again.")
...
```
**AJAX GET**
- Melakukan modifikasi `views.py` pada `main` dengan mengubah fungsi `show_json` dan `show_xml`, serta  menambahkan fungsi `add_product_ajax`
```py
...
def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    stock = request.POST.get("stock")
    user = request.user

    new_product = Product(
        name=name, price=price,
        description=description, stock=stock,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
...
```
- Melakukan modifikasi `views.py` pada `main` dengan menambahkan impor dan path ke `urlpatterns` untuk menambahkan routing
```py
from main.views import add_product_ajax
...
urlpatterns = [
    ...
    path('add-product-ajax', add_product_ajax, name='add_product_ajax')
]
```
- Melakukan modifikasi `main.html` pada `main/templates` dengan menghapus block conditional `product` dan mengganti dengan `<div id="product_cards"></div>`, serta penambahan Product dengan AJAX
```html
<div id="product_cards" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"></div>
...
    <!-- Modal body -->
    <div class="px-6 py-4 space-y-6 form-style">
      <form id="productForm" class="space-y-6">
        {% csrf_token %}
        <div class="flex flex-col">
          <label for="name" class="mb-2 font-semibold text-gray-700">
            Name
          </label>
          <input type="text" id="name" name="name" class="w-full border border-gray-300 rounded-md p-2 focus:border-green-800" required>
        </div>
        <div class="flex flex-col">
          <label for="price" class="mb-2 font-semibold text-gray-700">
            Price
          </label>
          <input type="number" id="price" name="price" class="w-full border border-gray-300 rounded-md p-2 focus:border-green-800" required>
        </div>
        <div class="flex flex-col">
          <label for="description" class="mb-2 font-semibold text-gray-700">
            Description
          </label>
          <textarea id="description" name="description" rows="3" class="w-full border border-gray-300 rounded-md p-2 focus:border-green-800" required></textarea>
        </div>
        <div class="flex flex-col">
          <label for="stock" class="mb-2 font-semibold text-gray-700">
            Stock
          </label>
          <input type="number" id="stock" name="stock" class="w-full border border-gray-300 rounded-md p-2 focus:border-green-800" required>
        </div>
      </form>
    </div>
```
- Melakukan modifikasi `main.html` pada `main/templates` dengan menambahkan fungsi JavaScript
```html
<script>
  async function getProduct(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }

  async function refreshProducts() {
    document.getElementById("product_cards").innerHTML = "";
    document.getElementById("product_cards").className = "";
    const products = await getProduct();
    let htmlString = "";
    let classNameString = "";

    if (products.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'images/sedih-banget.png' %}" alt="Sad face" class="w-64 h-64 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada product yang ditambahkan</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        products.forEach((item) => {
          const name = DOMPurify.sanitize(item.fields.name);
          const description = DOMPurify.sanitize(item.fields.description);

            htmlString += `
              <div class="bg-white shadow-lg rounded-lg overflow-hidden border-2 border-green-800 transform hover:scale-105 transition-transform duration-300">
                <div class="p-4 bg-green-700 text-white">
                  <h3 class="font-bold text-lg mb-2">${name}</h3>
                  <p class="text-sm">Price: Rp${item.fields.price}</p>
                  <p class="text-sm">Stock: ${item.fields.stock}</p>
                </div>
                <div class="p-4">
                  <p class="text-gray-700 mb-4">${description}</p>
                  <div class="flex justify-between items-center">
                    <a href="/edit-product/${item.pk}" class="bg-yellow-400 hover:bg-yellow-500 text-white rounded-lg py-2 px-4 transition duration-300 shadow-md">Edit</a>
                    <a href="/delete-product/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-lg py-2 px-4 transition duration-300 shadow-md">Delete</a>
                  </div>
                </div>
              </div>`;
        });
    }
    document.getElementById("product_cards").className = classNameString;
    document.getElementById("product_cards").innerHTML = htmlString;
  }

refreshProducts();
</script>
```
- Melakukan modifikasi pada `main.html` pada `main/templates/` untuk membersihkan data dengan DOMPurify
```html
{% block meta %}
<title>Every Mart</title>
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
{% endblock meta %}
```
**AJAX POST**
- Melakukan modifikasi `views.py` pada `main` dengan menambahkan impor dan fungsi `add_product_ajax`
```py
...
@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    stock = request.POST.get("stock")
    user = request.user

    new_product = Product(
        name=name, price=price,
        description=description, stock=stock,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
    ...
```
- Melakukan modifikasi `views.py` pada `main` dengan menambahkan impor dan path ke `urlpatterns` untuk menambahkan routing
```py
from main.views import add_product_ajax
...
urlpatterns = [
    ...
    path('add-product-ajax', add_product_ajax, name='add_product_ajax')
]
```
- Melakukan modifikasi `main.html` pada `main/templates` untuk menambahkan Button dan Modal Form
```html
  <div class="flex flex-col sm:flex-row justify-end items-center gap-4 mb-6">
    <a href="{% url 'main:create_product' %}" class="bg-green-800 hover:bg-yellow-400 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
      Add Product
    </a>
    <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="bg-green-700 hover:bg-red-500 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
      Add Product by AJAX
    </button>
  </div>
...

<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
  <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
    <!-- Modal header -->
    <div class="flex items-center justify-between p-4 border-b rounded-t bg-green-800">
      <h3 class="text-xl font-semibold text-white">
        Add Product
      </h3>
      <button type="button" class="text-white bg-transparent hover:bg-green-700 hover:text-gray-200 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 011.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
        </svg>
        <span class="sr-only">Close modal</span>
      </button>
    </div>
    <!-- Modal body -->
    <div class="px-6 py-4 space-y-6 form-style">
      <form id="productForm" class="space-y-6">
        {% csrf_token %}
        <div class="flex flex-col">
          <label for="name" class="mb-2 font-semibold text-gray-700">
            Name
          </label>
          <input type="text" id="name" name="name" class="w-full border border-gray-300 rounded-md p-2 focus:border-green-800" required>
        </div>
        <div class="flex flex-col">
          <label for="price" class="mb-2 font-semibold text-gray-700">
            Price
          </label>
          <input type="number" id="price" name="price" class="w-full border border-gray-300 rounded-md p-2 focus:border-green-800" required>
        </div>
        <div class="flex flex-col">
          <label for="description" class="mb-2 font-semibold text-gray-700">
            Description
          </label>
          <textarea id="description" name="description" rows="3" class="w-full border border-gray-300 rounded-md p-2 focus:border-green-800" required></textarea>
        </div>
        <div class="flex flex-col">
          <label for="stock" class="mb-2 font-semibold text-gray-700">
            Stock
          </label>
          <input type="number" id="stock" name="stock" class="w-full border border-gray-300 rounded-md p-2 focus:border-green-800" required>
        </div>
      </form>
    </div>
         
    <!-- Modal footer -->
    <div class="flex justify-end p-6 border-t border-gray-200 rounded-b">
      <button type="button" id="cancelButton" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg mr-2">
        Cancel
      </button>
      <button type="submit" id = "submitProduct" form="productForm" class="btn bg-green-700 hover:bg-green-800 text-white font-bold py-2 px-4 rounded-lg mr-2">
        Create Product
      </button>
    </div>
  </div>
</div>
```
- Modifikasi `main.html` dalam `main` dengan menambahkan fungsi JavaScript untuk mengirim data
```html
<script>
      async function getProduct(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }

    async function refreshProducts() {
    document.getElementById("product_cards").innerHTML = "";
    document.getElementById("product_cards").className = "";
    const products = await getProduct();
    let htmlString = "";
    let classNameString = "";

    if (products.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'images/sedih-banget.png' %}" alt="Sad face" class="w-64 h-64 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada product yang ditambahkan</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        products.forEach((item) => {
          const name = DOMPurify.sanitize(item.fields.name);
          const description = DOMPurify.sanitize(item.fields.description);

            htmlString += `
              <div class="bg-white shadow-lg rounded-lg overflow-hidden border-2 border-green-800 transform hover:scale-105 transition-transform duration-300">
                <div class="p-4 bg-green-700 text-white">
                  <h3 class="font-bold text-lg mb-2">${name}</h3>
                  <p class="text-sm">Price: Rp${item.fields.price}</p>
                  <p class="text-sm">Stock: ${item.fields.stock}</p>
                </div>
                <div class="p-4">
                  <p class="text-gray-700 mb-4">${description}</p>
                  <div class="flex justify-between items-center">
                    <a href="/edit-product/${item.pk}" class="bg-yellow-400 hover:bg-yellow-500 text-white rounded-lg py-2 px-4 transition duration-300 shadow-md">Edit</a>
                    <a href="/delete-product/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-lg py-2 px-4 transition duration-300 shadow-md">Delete</a>
                  </div>
                </div>
              </div>`;
        });
    }
    document.getElementById("product_cards").className = classNameString;
    document.getElementById("product_cards").innerHTML = htmlString;
  }

refreshProducts();

const modal = document.getElementById('crudModal');
const modalContent = document.getElementById('crudModalContent');

function showModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modal.classList.remove('hidden'); 
    setTimeout(() => {
      modalContent.classList.remove('opacity-0', 'scale-95');
      modalContent.classList.add('opacity-100', 'scale-100');
    }, 50); 
}

function hideModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
      modal.classList.add('hidden');
    }, 150); 
}
</script>
```
- Menampilkan daftar Product dengan `product_cards`
```html
<div id="product_cards" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"></div>
```
**Github dan PWS**
- Mengunggah perubahan pada repositori GitHub dan melakukan push ke PWS
```
git add .
git commit -m "..."
git push origin main

git branch -M main
git push pws main:master
```
<hr>

</details>

<details>
<summary> <strong> Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS </strong> </summary>

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, urutan prioritas pengambilan:
1. Inline Style <br>
    Inline style didefinisikan langsung pada elemen HTML menggunakan atribut `style` dan memiliki prioritas tertinggi
2. ID Selectors <br>
    ID Selectors menggunakan atribut `id` dari suatu elemen dan ditandai dengan awalan `#`
3. Classes dan Pseudo-classes <br>
    Classes dan Pseudo-classes menggunakan nama `class` atau pseudo-classes dan ditandai dengan awalan `.`
4. Attributes <br>
    Attributes yang biasa digunakan pada attributes HTML
5. Elements dan pseudo-elements <br>
    Elements dan pseudo-elements memiliki prioritas rendah dan akan digunakan jika tidak ada style lain yang didefinisikan

Contoh:
```html
<!DOCTYPE html>
<html>

<head>
    <style type="text/css">
        p {
            color: black;
        }

        .class-selector {
            color: blue;
        }

        #id-selector {
            color: green;
        }

        [type="text"] {
            color: purple;
        }

        p:hover {
            color: orange;
        }
    </style>
</head>

<body>
    <p style="color: red;" id="id-selector" class="class-selector" type="text">
        Urutan prioritas CSS selector
    </p>
</body>

</html>
```
Referensi: [CSS Specificity](https://www.geeksforgeeks.org/css-specificity/)
<hr>

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena munculnya beragam perangkat dengan berbagai ukuran layar, seperti desktop, tablet, dan ponsel utnuk mengakses internet. Dengan adanya responsive design, aplikasi web dapat beradaptasi secara otomatis, menampilkan tampilan dan fungsionalitas yang optimal di semua perangkat. Hal ini dapat meningkatkan kenyamanan pengguna dan memastikan konsistensi penggalaman pengguna terlepas dari perangkat yang digunakan.
Banyak aplikasi populer sudah menerampkan responsive design, seperti YouTube, Twitter, Instagram, dan LinkedIn. Contoh lain aplikasi yang sudah menerapkan responsive design adalah SCeLE (Student Centered e-Learning Environment) yang digunakan sebagai media pembelajaran online yang ada di Fasilkom UI. Di sisi lain, ada aplikasi yang belum menerapkan responsive design, yaitu SIAKNG (Sistem Informasi Akademik Next Generation) untuk membantu menunjang kegiatan akademik di Universitas Indonesia. Aplikasi web ini masih menampilkan versi desktop yang tidak optimal ketika diakses melakui mobile. Hal ini mengharuskan pengguna melakukan zoom in dan scrolling berlebihan. Contoh lain aplikasi yang belum menerapkan responsive design adalah Pacil Web Service (PWS) yang digunakan dalam mata kuliah Pemrograman Berbasis Platform (PBP). Hal ini mengakibatkan pengguna perlu membuka aplikasi web tersebut dalam layar penuh pada desktop.
<hr>

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
![Margin, Border, dan Padding](/margin,border,padding.webp)
| **Komponen** | **Detail** | **Contoh implementasi** |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **Margin**   | Ruang di luar elemen yang memisahkan elemen satu dengan lainnya. Margin memiliki fungsi untuk mengatur jarah antar elemen dan tidak memperngaruhi ukuran elemen. |`margin: 10px 20 px 15 px 20 px;`|
| **Border**   | Garis yang mengelilingi elemen untuk memberikan batas visual pada elemen. Border dapat diatur ketebalan, warna, dan gaya, serta menambah ukuran total elemen |`border: 2px solid black;`|
| **Padding**  | Ruang di antara konten dan border di dalam elemen. Padding berfungsi untuk memberikan jarak internal antara konten dan batas elemen, meningkatkan keterbacaan dan estetika konten. Padding hanya menggeser konten dan transparan. |`padding: 10px;`|
<hr> 

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flex box dan grid layout adalah metode modern dalam CSS untuk menciptakan tata letak responsif dan fleksibel pada aplikasi web.
Flexbox dan Grid Layout adalah dua metode modern dalam CSS yang digunakan untuk menciptakan tata letak responsif dan fleksibel pada website. Keduanya memiliki karakteristik dan kegunaan yang berbeda: <br>
- **Flexbox (Flexible Box Layout)**
    - Flexbox adalah sistem tata letak satu dimensi yang fokus pada pengaturan elemen dalam satu baris atau kolom.
    - Kegunaan flexbox:
        1. Menyusun elemen secara horizontal atau vertikal dengan mudah.
        2. Mengatur penyebaran ruang antar elemen secara otomatis.
        3. Menyelaraskan elemen di dalam kontainer.
    - Flexbox dangat fleksibel untuk tata letak sederhana dan responsif, sehingga ideal untuk komponen UI seperti navigation bar, menu, atau daftar item. <br>
- **Grid Layout**
    - Grid layout adalah sistem tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom secara bersamaan.
    - Kegunaan grid layout:
        1. Membuat layout halaman yang kompleks dengan mudah.
        2. Mengatur elemen dalam grid yang terdefinisi.
        3. Menempatkan elemen pada posisi spesifik dalam layout.
    - Grid layout memberikan kontrol yang lebih presisi atas penempatan elemen dalam dua dimensi, sehingga cocok untuk desain dashboard, galeri foto, atau layout halaman utama. <br>
<hr>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
**Menyambungkan template Django dengan Tailwind**
- Melakukan modifikasi `base.html` pada `main/templates`
```html
<head>
{% block meta %}
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
{% endblock meta %}
<script src="https://cdn.tailwindcss.com">
</script>
</head>
</details>
```
**Menambahkan fitur `Edit Product` dan `Hapus Product`**
- Melakukan modifikasi `views.py` dalam `main` dengan menambahkan fungsi `edit_product` dan `hapus_product` serta menambahkan import
``` py
from django.shortcuts import .., reverse
from django.http import .., HttpResponseRedirect
...
def edit_product (request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    
    # Set product sebagai isntance dari form
    form = ProductEntryForm(request.POST or None, instance = product)
    
    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    
    # Hapus product
    product.delete()
    
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```
- Menambahkan berkas `edit_product.html` dalam `main/templates`
```html
{% extends 'base.html' %}
{% load static %}
{% block content %}

<h1>Edit Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Mood"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
- Modifikasi `urls.py` dalam `main` dengan import fungsi `edit_product` dan `delete_product`, serta menambahkan path url ke `urlpatterns`
```py
from main.views import edit_product, delete_product
...
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
```
- Modifikasi `main.html` dalam `main/templates`
```html
    ...
    <td>
        <a href="{% url 'main:edit_product' product.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
    <td>
        <a href="{% url 'main:delete_product' product.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
...
```
**Melakukan modifikasi pada template HTML menggunakan Tailwind**
- Menambahkan Navigation Bar dengan membuat berkas `navbar.html` pada `main/templates` dan menautkan navbar dengan `main.html`, `create_product.html`, dan `edit_html`
- Modifikasi `settings.py` untuk konfigurasi Static Files
```py
...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
...
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static'
...
```
- Membuat `global.css` dalam `/static/css`, lalu menghubungkan `global.css` dan script Tailwind ke `base.html` untuk menambahkan Styles
`base.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
`global.css`
```css
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
    background-color: #f9fafb;
    font-size: 1rem;
    font-family: 'Helvetica', 'Arial', sans-serif;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #f39c12;
    box-shadow: 0 0 8px rgba(243, 156, 18, 0.4);
}
button, 
.form-style form button {
    background-color: #f39c12;
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 0.375rem;
    font-size: 1rem;
    font-weight: bold;
    font-family: 'Helvetica', 'Arial', sans-serif;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover, 
.form-style form button:hover {
    background-color: #e67e22;
    transform: scale(1.05);
}
@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
.animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
    background-size: 200% 100%;
    animation: shine 3s infinite;
}
```
- Melakukan styling pada `login.html`, `register.html`, `card_info.html`, `card_product.html`, `create_product.html`, `edit_product.html`
**Github dan PWS**
- Mengunggah perubahan pada repositori GitHub dan melakukan push ke PWS
```
git add .
git commit -m "..."
git push origin main

git branch -M main
git push pws main:master
```
<hr>
</details>

<details>
<summary> <strong> Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django </strong> </summary>

### Apa perbedaan antara HttpResponseRedirect() dan redirect()
**HttpResponseRedirect()** <br>
`HttpResponseRedirect()` mengembalikan objek dengan kode status 302, yang memberi instruksi untuk melakukan pengalihan ke URL tertentu secara manual. `HttpResponseRedirect()` umumnya digunakan ketika terdapat URL yang ingin dituju (absolute path), sehingga tidak memerlukan penanganan tambahan dari Django.
Contoh implementasi `HttpResponseRedirect()`:
```py
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # HttpResponseRedirect ke URL
            return HttpResponseRedirect(reverse('main:show_main'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
```
**redirect()** <br>
`redirect()` merupakan helper function yang disediakan oleh Djangodengan berbagai parameter. `redirect()` cenderung lebih fleksibel karena dapat menerima berbagai parameter, seperti model, view, dan URL. Django akan melakukan konversi parameter yang diberikan menjadi URL, lalu mengembalikan `HttpResponseRedirect()`.
Contoh implementasi `redirect()`:
```py
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            # Redirect ke view
            return redirect('main:login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})
```
Dapat disimpulkan bahwa `HttpResponseRedirect()` memerlukan URL secara eksplisit, sedangkan `redirect()` dapat menerima berbagai parameter sehingga lebih fleksibel.
<hr>

### Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model `Product` dengan User dilakukan dengan menggunakan **ForeignKey**, yang mencipatakan relasi **many-to-one**. Relasi ini memungkinkan User memiliki banyak Product, tetapi satu Product hanya dimiliki satu User.
Setiap kali User membuat entri Product, maka Product tersebut secara otomatis terhubung dengan User yang sedang login melalui atribut `user`. Atribut `user` dalam model `Product` merujuk ke model `User` dengan `ForeignKey(User, on_delete=models.CASCADE)`, memastikan bahwa Product tersebut dimiliki oleh satu pengguna tertentu. Ketika User dihapus, Product yang ditambahkan oleh User tersebut juga akan dihapus dengan `on_delete=models.CASCADE`. 
Contoh implementasi penghubungan model `Product` dengan User:
```py
class Product(models.Model) :
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   mood = models.CharField(max_length=255)
   time = models.DateField(auto_now_add=True)
   feelings = models.TextField() 
```
<hr>

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

**Authentication** <br>
Authentication adalah proses verifikasi identitas User. Untuk melakukan authentication, User akan diminta untuk memasukkan kredensial seperti username dan passowrd. Kemudian, Django menggunakan fungsi `authenticate()` untuk melakukan verifikasi kredensial dan `login()` untuk mencatat User. Setelah login berhasil, informasi User akan disimpan dalam **session**.
**Authorization** <br>
Authorization adalah proses penetuan hak akses atau izin User untuk mengakses fitur atau data tertentu. Setelah melakukan authentication, Django akan menyimpan informasi User untuk authorization. Django menggunakan permissons dan groups, serta decorator seperti `@login_required` untuk mengatur hak akses atau izin User. 
<hr>

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat User yang telah login melalui mekanisme **session** yang dikelola oleh **cookies**. Setelah User telah berhasil login, Django akan membuat **session ID** yang disimpan di server dan ditempatkan dalam **cookies** di browser. Setiap kali User membuat request baru, maka browser akan mengirimkan **session ID** sehingga Django dapat melakukan identifikasi User tanpa mengharuskan User untuk login kembali.
Selain mengingat User yang telah login, cookies memili beberapa kegunaan lain, yaitu:
- **Menyimpan preferensi pengguna** <br>
  Cookies dapat menyimpan preferensi pilihan User, seperti preferensi tampilan atau bahasa yang digunakan
- **Melacak aktivitas pengguna** <br>
  Cookies dapat menyimpan data tentang halaman yang telah dikunjungi oleh User
- **Fitur 'Remember Me'** 
  Cookies memungkinkan User untuk tetap login meskipun User telah menutup dan membuka kembali browser

Namun, **tidak semua cookies aman digunakan**. Salah satu contoh cookies yang tidak aman adalah  **cookies tanpa atribut HttpOnly** yang rentan terhadap serangan XSS (Cross Site Scripting) karena dapat diakses oleh JavaScript yang berpotensi berbahaya. Oleh karena itu, penting untuk menerapkan pengaturan seperti Secure, HttpOnly, dan SameSite agar dapat mengurangi risiko keamanan.
<hr>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**Fungsi dan form registrasi pengguna**
- Menambahkan import pada `views.py` dalam `main`
```py
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
- Menambahkan fungsi `register` dalam `views.py` untuk otomasisasi form registrasi pengguna
```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
- Membuat `register.html` dalam `main/templates` untuk form registrasi pengguna
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
- Memodifikasi `urls.py` dalam `main` dengan menambahkan import dan path url untuk konfigurasi URL
```py
from main.views import register
...
    urlpatterns = [
        ...
        path('register/', register, name='register'),
    ]
```
**Fungsi login pengguna**
- Memodifikasi `views.py` dalam `main` dengan menambahkan import dan fungsi `login_user`
```py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
...
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('main:show_main')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```
- Membuat berkas `login.html` dalam `main/templates` untuk login pengguna
```py
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
- Memodifikasi `urls.py` dalam `main` dengan menambahkan import dan path url untuk konfigurasi URL
```py
from main.views import login_user
...
    urlpatterns = [
    ...
    path('login/', login_user, name='login'),
    ]
```
**Fungsi logout pengguna**
- Memodifikasi `views.py` dalam `main` dengan menambahkan import dan modifikasi fungsi `logout_user`
```py
from django.contrib.auth import logout
...
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
- Memodifikasi `main.html` dalam `main/templates` untuk menambahkan hyperlink tag
```py
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
- Memodifikasi `urls.py` dalam `main` dengan menambahkan import dan path url untuk konfigurasi URL
```py
from main.views import logout_user
...
    urlpatterns = [
    ...
    path('logout/', logout_user, name='logout'),
    ]
```
**Restriksi akses**
- Modifikasi `views.py` dalam `main`
```py
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')
```
- Modifikasi `views.py` dalam `main` untuk menambahkan data last login pengguna dengan menambahkan impor, modifikasi fungsi `login_user`, modifikasi `show_main`, serta modifikasi `logout_user`
```py
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
context = {
    'name': 'Pak Bepe',
    'class': 'PBP D',
    'npm': '2306123456',
    'mood_entries': mood_entries,
    'last_login': request.COOKIES['last_login'],
}
```
**Data dari cookies**
- Modifikasi `main.html` dalam `main/templates` untuk menampilkan data last login
```
<h5>Sesi terakhir login: {{ last_login }}</h5>
```
**Menghubungkan Model `Product` dengan User**
- Modifikasi `models.py` dalam `main`
```
from django.contrib.auth.models import User
...
class Product(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
- Modifikasi `views.py` dalam `main` dengan modifikasi fungsi `create_product` dan fungsi `show_main`
```py
def show_main(request):
    products = Product.objects.all()
    context = {
        'npm' : '2306229405',
        'name': request.user.username,
        'class': 'PBP D',
        'products' : products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
...
def create_product(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        mood_entry = form.save(commit=False)
        mood_entry.user = request.user
        mood_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```
- Melakukan migrasi model (dengan syarat minimal satu user dalam database) pada terminal
```
python manage.py makemigrations
python manage.py migrate
```
- Modifikasi `settings.py` dalam `mental_health_tracker` dengan menambahkan import dan mengganti variabel
```py
import os
...
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```
**Github dan PWS**
- Mengunggah perubahan pada repositori GitHub dan melakukan push ke PWS
```
git add .
git commit -m "..."
git push origin main

git branch -M main
git push pws main:master
```
<hr>
</details>

<details>
<summary> <strong> Tugas 3: Implementasi Form dan Data Delivery pada Django </strong> </summary>

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery memungkinkan pertukaran informasi yang akurat dan efisien antara user, sistem, dan perangkat. Hal ini menjamin integritas data, meningkatkan kecepatan transfer dan mengoptimalkan penggunaan sumber daya platform. Mekanisme data delivery mendukung terjadinya pertukaran informasi secara mulus antara berbagai komponen, terutama antara front-end dan back-end. Dengan data delivery, sebuah platform dapat berfungsi secara optimal karena informasi yang masuk dapat dikelola dengan baik.
<hr>

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik dari XML dengan beberapa alasan, yaitu:
1. JSON menggunakan format yang lebih ringkas dibandingkan XML sehingga JSON memungkinkan representasi data yang sama dengan karakter yang lebih sedikit
2. JSON lebih mudah di-parse oleh beberapa bahasa pemrograman sehingga proses pengolahan data lebih cepat
3. JSON memiliki readibility yang tinggi sehingga mudah dibaca dan dipahami oleh pengguna
4. JSON mendukung beberapa tipe data seperti string, object, dan array
Dapat disimpulkan bahwa JSON lebih populer dibandingkan XML karena efisiensi yang ditawarkannya. Struktur data JSON yang sederhana tetapi memiliki banyak keunggulan membuat JSON menjadi pilihan utama dalam pengembangan platform. 
<hr>

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method 'is_valid()' memiliki peranan penting untuk melakukan validasi data yang pengguna masukkan pada form. Apabila data yang dimasukkan pengguna tidak sesuai, method ini akan mengembalikan nilai 'False'. Sedangkan, apabila data yang dimasukkan pengguna sesuai, method ini akan mengembalikan nilai 'True' dan input data akan diproses di dalam 'Product Entry Form' yang akan mengarah ke 'models'. 
Dengan demikian, method 'is_valid()' diperlukan untuk menjaga keamanan dan konsistensi data. Hal ini juga akan mempermudah dalam proses pemeliharaan yang dilakukan oleh para pengembang platform.
<hr>

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` diperlukan saat membuat form di Django sebagai perlindungan dari serangan Cross-Site Request Forgery (CSRF). Tanpa adanya `csrf_token` pada form, platform menjadi rentan terhadap eksploitasi dimana penyerang dapat membuat `request` dengan mudah tanpa sepengetahuan pengguna karena tidak dilakukan pengecekan `request` terlebih dahulu. Mekanisme `csrf_token` melibatkan penyisipan token unik ke dalam form HTML, yang akan diverifikasi saat `request` diterima. Token unik ini tidak dapat diketahui oleh penyerang sehingga menyulitkan penyerang untuk melakukan `request` tanpa sepengetahuan pengguna. Dengan demikian, `csrf_token` sangat krusial untuk menjaga integritas dan keamanan platform agar terhindar dari CSRF. 
<hr>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Mengubah primary key dari integer menjadi UUID untuk best practice dari sisi keamanan aplikasi dengan melakukan modifikasi `models.py`
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
- Melakukan migrasi model melalui terminal
```
python manage.py makemigrations
python manage.py migrate
```
- Membuat `forms.py` dalam `main` untuk menerima Product Entry Form baru
```py
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock"]
```
- Melakukan modifikasi dengan menambahkan import pada `views.py` dalam `main`
```py
from django.shortcuts import render, redirect
```
- Melakukan modifikasi pada `views.py` dalam `main` dengan menambahkan fungsi `create_product` untuk menghasilkan form yang dapat menambahkan Product Entry secara otomatis
```py
def create_product(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```
- Melakukan modifikasi pada `views.py` dalam `main` dengan mengubah fungsi `show_main`
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
- Melakukan modifikasi pada `urls.py` dalam `main` dengan menambahkan import dan menambahkan path URL
```py
from main.views import show_main
```
```py
    path('create-product', create_product, name='create_product'),
```
- Membuat 'create_product.html' dalam 'main/templates'
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
- Menjalankan proyek Django melalui terminal untuk mengecek fungsionalitas
```
python manage.py runserver
```
- Melakukan modifikasi `main.html` dalam `main/templates` untuk menampilkan data dalam bentuk table serta tombol `Add New Product`
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
- Melakukan modifikasi pada `views.py` dalam `main` dengan menambahkan import dan menambahkan fungsi `show_xml` untuk mengembalikan data dalam bentuk XML
``` py
from django.http import HttpResponse
from django.core import serializers
```
``` py
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
- Melakukan modifikasi pada `urls.py` dalam `main` dengan menambahkan import dan menambahkan path URL untuk konfigurasi routing URL
```py
from main.views import show_main, create_mood_entry, show_xml
```
```py
    path('xml/', show_xml, name='show_xml'),
```
- Melakukan modifikasi pada `views.py` dalam `main` dengan menambahkan fungsi `show_json` untuk mengembalikan data dalam bentuk JSON
```py
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Melakukan modifikasi pada `urls.py` dalam `main` dengan menambahkan import dan menambahkan path URL untuk konfigurasi routing URL
```py
from main.views import show_main, create_mood_entry, show_xml, show_json
```
```py
    path('json/', show_json, name='show_json'),
```
- Melakukan modifikasi pada `views.py` dalam `main` dengan menambahkan fungsi `show_xml_by_id` dan `show_json_by_id` untuk menerima parameter `request` dan `id` untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON
```py
def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Melakukan modifikasi pada `urls.py` dalam `main` dengan menambahkan import dan menambahkan path URL untuk konfigurasi routing URL
```py
from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
```
```py
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```
- Menjalankan proyek Django melalui terminal untuk mengecek fungsionalitas dan menggunakan Postman sebagai Data Viewer
```
python manage.py runserver
```
- Mengunggah perubahan pada repositori GitHub dan melakukan push ke PWS
```
git add .
git commit -m "..."
git push origin main

git branch -M main
git push pws main:master
```
<hr>

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
###### XML
![XML](/xml.png)
###### JSON
![JSON](/json.png)
###### XML by ID
![XML by ID](/xml_id.png)
###### JSON by ID
![JSON by ID](/json_id.png)
<hr>
</details>

<details>
<summary> <strong> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </strong> </summary>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
- Membuat direktori lokal bernama `every-mart` dan masuk ke direktori tersebut melalui terminal
```
cd <path_direktori>\every-mart
```
- Melakukan konfigurasi nama pengguna dan alamat email agar terhubung dengan Git

```
git config --global user.name "<NAME>"
git config --global user.email "<EMAIL>"
```
- Membuat repositori GitHub dengan nama `every-mart` dan menghubungkan dengan direktori lokal
```
git branch -M main
git remote add origin https://github.com/deanitasekar/every-mart.git
```
- Memulai instalasi Django dengan mengaktifkan virtual environment
```
python -m venv env
env\Scripts\activate
```
- Menyiapkan dependencies dengan membuat berkas `requirements.txt` dan melakukan instalansi dependencies
```
pip install -r requirements.txt
```
- Membuat proyek Django bernama `every_mart`
```
django-admin startproject every_mart .
```
- Melakukan modifikasi pada `ALLOWED_HOTS` di `settings.py` untuk deployment dan menjalankan server Django
```
python manage.py runserver
```
- Membuat aplikasi bernama `main` dalam proyek dan melakukan modifikasi pada `INSTALLED_APPS` di `settings.py` dalam direktori
```
python manage.py startapp main
```
- Membuat `main.html` dan mengisi sesuai dengan kode yang diharapkan
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
- Melakukan modifikasi 'models.py' dalam direktori aplikasi 'main'
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
- Melakukan migrasi model untuk mengaplikasikan models ke dalam basis data
```
python manage.py makemigrations
python manage.py migrate
```
- Mengintegrasikan komponen MVT dengan melakukan modifikasi `views.py` dalam direktori aplikasi `main`
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
- Mengonfigurasi routing URL aplikasi `main` dengan membuat berkas `urls.py`
```py
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
- Mengonfigurasi routing URL proyek dengan melakukan modifikasi `urls.py` dalam direktori `every_mart`
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
- Mencoba proyek Django secara lokal
```
python manage.py runserver
```
- Menambahkan berkas `.gitignore` dan mengunggah proyek ke repositori Github `every-mart`
```
git add .
git commit -m "..."
git push origin main
```
- Mengakses halaman PWS pada https://pbp.cs.ui.ac.id.dan membuat proyek baru dengan nama `everymart`
- Melakukan modifikasi `settings.py` pada `ALLOWED_HOSTS` untuk menghubungkan dengan URL deployment PWS
```py
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "deanita-sekar-everymart.pbp.cs.ui.ac.id"]
```
- Mengunggah perubahan pada repositori GitHub dan melakukan push ke PWS
```
git add .
git commit -m "..."
git push origin main

git branch -M main
git push pws main:master
```
<hr>

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
`urls.py` berfungsi sebagai peta dalam web aplikasi dan menghubungkan pola URL sesuai dengan `views.py`. `views.py` menangani HTTP Request dan mengembalikan respons, serta berinteraksi dengan `models.py` untuk memodifikasi data. `models.py` akan menyediakan abstraksi untuk interaksi dengan database. `berkas html` akan menentukan bagaimana data dari `views.py` ditampilkan kepada Client.
<hr>

### Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah alat software development yang memiliki fungsi sebagai version control system untuk melacak dan mengelola source code secara efisien. Dalam pengembangan perangkat lunak, Git memiliki beberapa peranan penting, yaitu:
- Git membantu pelacakan perubahan kode dengan informasi lengkap tentang apa yang diubah, siapa yang melakukan perubaham, dan kapan dilakukan perubahan
- Git memudahkan dalam melakukan branching karena dapat membuat branch baru untuk keperluan pengembangan perangkat lunak dan branch tersebut dapat di-merge apabila diperlukan
- Git menyimpan riwayat perubahan kode pada setiap commit yang dilakukan sehingga dimungkinkan untuk kembali ke versi sebelumnya apabila diperlukan
- Git menyediakan berbagai fitur yang dapat memudahkan kolaborasi dalam waktu yang bersamaan untuk mempermudah pengembangan perangkat lunak dengan banyak developer
<hr>

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django sebagai permulaan pembelajaran pengembangan perangkat lunak menawarkan kombinasi unik yang jarang ditemui pada framework lain. Penggunaan bahasa pemrograman Python memberi kemudahan karena sintaksnya bersih sehingga developer dapat mempelajari pengembangan perangkat lunak tanpa terjebak dalam sintaks yang rumit. 
Framework Django memiliki arsitektur MVT (Model-View-Template) menghadirkan struktur yang logis dan intuitif untuk memahami alur pengembangan perangkat lunak. Selain itu, adanya ORM (Object-Relational Mapping) dapat membuat interaksi dengan database menjadi lebih mudah karena developer tidak perlu menulis kode SQL secara langsung. Tidak terbatas di situ saja, framework ini memiliki keunggulan dengan keamanan yang terintegrasi secara default. 
Berdasarkan pengamatan saya selama beberapa minggu perkuliahan PBP, saya meyakini bahwa framework Django dapat menjadi framework yang paling cocok untuk memulai pembelajaran dalam pengembangan perangkat lunak dan memiliki potensi besar untuk pengembangan perangkat lunak lanjutan.
<hr>

### Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena perannya sebagai jembatan penghubung antara objek dalam Python dengan database relasional. ORM Django memungkinkan developer untuk mendefinisikan struktur data dan relasi menggunakan Python yang secara otomatis diterjemahkan ke dalam skema database dan operasi SQL yang sesuai. Mekanisme ini memudahkan developer untuk berinteraksi dengan databse menggunakan Python tanpa perlu menulis query SQL kompleks secara langsung. ORM yang dimiliki oleh Django membantu developer untuk berfokus pada pengembangan perangkat lunak daripada implementasi database.
<hr>
