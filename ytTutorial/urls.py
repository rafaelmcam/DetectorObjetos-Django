"""ytTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from pages.views import home_view, page1_view, about_view
from products.views import product_detail_view, product_create_view, dynamic_lookup_view, product_delete_view, product_list_view, detec_view

urlpatterns = [
    path("", home_view, name = "home"),
    path("page1/", page1_view),
    path("about/", about_view),
    path("create/", product_create_view),
    path("product/", product_list_view, name = "product_main"),
    path("product/<int:my_id>/", dynamic_lookup_view, name = "dynamic_view"),
    path("product/<int:my_id>/delete", product_delete_view, name = "dynamic_delete"),
    path("detec/", detec_view, name = "detec_page"),
    path('admin/', admin.site.urls),
]

# Configuracao para os arquivos de media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print("URL PATTERNS: \n\n\n", urlpatterns)