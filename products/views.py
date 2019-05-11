from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Opencv
from .forms import ProductForm, RawProductForm, FormOpencv

# Create your views here.

import matplotlib.pyplot as plt
import numpy as np 
import math
import os
import glob
import cv2
from imageai.Detection import ObjectDetection

def recebe_imagem(obj):
    imagem_db = obj.imagem
    print(imagem_db)
    imagem_read = imagem_db.read() # type 'str'
    imagem_np = np.asarray(bytearray(imagem_read), dtype="uint8") # type 'numpy.ndarray'
    imagem_op = cv2.imdecode(imagem_np, cv2.IMREAD_COLOR) # type 'numpy.ndarray'

    # retorna imagem para procesamento
    return imagem_op

def detec_view(request):
    form = FormOpencv(request.POST or None, request.FILES or None)
    if form.is_valid():

        obj = Opencv(imagem = request.FILES['imagem'])
        print(obj)
        imagem = recebe_imagem(obj)


        model_weight_path = "resnet50_v2.0.1.h5"
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(model_weight_path)
        detector.loadModel()

        img = imagem.copy()
        detections = detector.detectObjectsFromImage(input_type = "array", input_image = img, minimum_percentage_probability = 90)
        #print(detections)
        for det in detections:
            cv2.rectangle(img, tuple(det["box_points"][:2]), tuple(det["box_points"][2:]), (0, 0, 0), 5)
            cv2.putText(img, "{} - {}".format(det["name"], det["percentage_probability"]), tuple(det["box_points"][:2]), cv2.FONT_HERSHEY_PLAIN, 5,(0,0,255),3,cv2.LINE_AA)

        cv2.imwrite("products/static/img/original.png", imagem)
        cv2.imwrite("products/static/img/canny.png", img)

        data = True
        return render(request, 'filtros.html', {'form': form, 'data': data})

    else:
        form = FormOpencv()

    return render(request, 'products/filtros.html', {'form': FormOpencv})


# treino youtube tutorial

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