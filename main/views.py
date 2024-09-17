from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product

def show_main(request):
    products = Product.objects.all()
    context = {
        'npm' : '2306229405',
        'name': 'Deanita Sekar Kinasih',
        'class': 'PBP D',
        'products' : products,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
