from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import cv2
import numpy as np

def home_view(request, *args, **kwargs):
    # cv2.imshow("frame", np.zeros((400, 400)))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(request, args, kwargs)


    return render(request, "home.html", {})
    #return HttpResponse("<h1>Hello World</h1>")



def page1_view(request, *args, **kwargs):
    return HttpResponse("<font color = blue><center><h1>Page 1</h1></center>")

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})