from django import forms

class DataForm(forms.Form):
    datos = forms.CharField()
