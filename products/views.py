from django.shortcuts import render

from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

def product_create_view(request, *args, **kwargs):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)




# def product_create_view(request, *args, **kwargs):
#     #print(request.GET)
#     #print(request.POST)
#     #title = request.POST["title"]
#     if request.method == "POST":
#         my_new_title = request.POST["title"]
#         print(my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

# def product_create_view(request, *args, **kwargs):
#     form = ProductForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         "form": form
#     }
#     return render(request, "products/product_create.html", context)


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id = 1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description
    # }
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)