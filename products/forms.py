from django import forms
from .models import Product, Opencv

class FormOpencv(forms.ModelForm):
    class Meta:
        model = Opencv
        fields = ['imagem']

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label = "", widget = forms.TextInput(attrs = {"placeholder": "Digite Aqui"}))
    description = forms.CharField(  required = False,
                                    widget = forms.Textarea(attrs={
                                        "class": "new_class",
                                        "rows": 20,
                                        "placeholder": "Sua Descrição (Opcional)."
                                    })
                                 )
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]



class RawProductForm(forms.Form):
    title       = forms.CharField(label = "", widget = forms.TextInput(attrs = {"placeholder": "Digite Aqui"}))
    description = forms.CharField(  required = False,
                                    widget = forms.Textarea(attrs={
                                        "class": "new_class",
                                        "rows": 20
                                    })
                                 )
    price       = forms.DecimalField(initial = 199.99)