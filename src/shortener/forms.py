from django import forms

class SubmitURLForm(forms.Form):
    url = forms.CharField(label='Enviar URL')