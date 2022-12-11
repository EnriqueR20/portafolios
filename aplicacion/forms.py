from django import forms


# Mi formulario
class InputForm(forms.Form):
    Foto = forms.CharField(max_length=250)

    Titulo = forms.CharField(max_length=250)

    Descripción = forms.CharField(max_length=250)

    Tags = forms.CharField(max_length=50)

    URL_GIT = forms.URLField(max_length=250)
