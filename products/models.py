from django.db import models
from django.urls import reverse

# Create your models here.

class Opencv(models.Model):
    imagem = models.ImageField(upload_to="opencv/media")

class Product(models.Model):
    title       = models.CharField(max_length = 120)
    description = models.TextField(blank = True, null = True)
    price       = models.DecimalField(decimal_places = 2, max_digits = 1000)
    summary     = models.TextField(blank = False, null = True)
    featured    = models.BooleanField(default = False)
    new_featured= models.BooleanField(default = False)

    def get_absolute_url(self):
        return reverse("dynamic_view", kwargs={"my_id": self.id})
        #return "/product/{}".format(self.id)