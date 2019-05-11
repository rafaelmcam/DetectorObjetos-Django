from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Opencv
from .forms import ProductForm, RawProductForm, FormOpencv

# Create your views here.
import numpy as np
import cv2

def recebe_imagem(obj):
    # imagem.extencao
    imagem_db = obj.imagem
    print(imagem_db)
    imagem_read = imagem_db.read() # type 'str'
    imagem_np = np.asarray(bytearray(imagem_read), dtype="uint8") # type 'numpy.ndarray'
    imagem_op = cv2.imdecode(imagem_np, cv2.IMREAD_COLOR) # type 'numpy.ndarray'

    # retorna imagem para procesamento
    return imagem_op

def filtros_view(request):
    form = FormOpencv(request.POST or None, request.FILES or None)
    if form.is_valid():
        # class 'PDI.core_1.models.Opencv
        obj = Opencv(imagem = request.FILES['imagem'])
        print(obj)
        imagem = recebe_imagem(obj)

        # Processamento dos filtros com opencv e Python
        canny = cv2.Canny(imagem, 100, 200) # os segundo e terceiro argumentos são o limiar mínimo e máximo
        # filtro gaussiano
        gaussiano = cv2.GaussianBlur(imagem, (5,5), 0) # passa a imagem, o tamanho do kernel e o desvio padrão
        # filtro laplaciano
        laplaciano = cv2.Laplacian(imagem,cv2.CV_64F)
        # filtro sobel em x
        sobelx = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=5)
        # filtro sobel em y
        sobely = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=5)
        # negativo
        negativo = 255 - imagem

        cv2.imwrite("products/static/img/original.png", imagem)
        cv2.imwrite("products/static/img/canny.png", canny)
        # cv2.imwrite("PDI/core_1/static/img/original.png", imagem)
        # cv2.imwrite("PDI/core_1/static/img/canny.png", canny)
        # cv2.imwrite("PDI/core_1/static/img/laplaciano.png", laplaciano)
        # cv2.imwrite("PDI/core_1/static/img/gaussiano.png", gaussiano)
        # cv2.imwrite("PDI/core_1/static/img/sobelx.png", sobelx)
        # cv2.imwrite("PDI/core_1/static/img/sobely.png", sobely)
        # cv2.imwrite("PDI/core_1/static/img/negativo.png", negativo)

        data = True
        return render(request, 'filtros.html', {'form': form, 'data': data})

    else:
        form = FormOpencv()

    return render(request, 'products/filtros.html', {'form': FormOpencv})


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id = my_id)
    print(obj.title)
    # print(request, my_id)
    # print(request.method)
    if request.method == "POST":
        # print("BLA2")
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_dynamic_delete.html", context)



def dynamic_lookup_view(request, my_id, *args, **kwargs):
    #obj = Product.objects.get(id = my_id)
    obj = get_object_or_404(Product, id = my_id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

# def product_create_view(request, *args, **kwargs):
#     initial_data = {
#         "title": "My awesome title"
#     }
    
#     obj = Product.objects.get(id = 1)

#     form = ProductForm(request.POST or None, instance = obj)
#     if form.is_valid():
#         form.save()
#     context = {
#         "form": form
#     }
#     return render(request, "products/product_create.html", context)



def product_create_view(request, *args, **kwargs):
    my_form = RawProductForm()
    print("BLA")
    if request.method == "POST":
        print("BLA2")
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
#         print(form.cleaned_data.get("title"))
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