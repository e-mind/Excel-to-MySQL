from django import forms

class DataForm(forms.Form):
    encriptar = forms.CharField()
    desencriptar = forms.CharField()
