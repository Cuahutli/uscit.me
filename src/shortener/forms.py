from django import forms
from .validators import validate_dot_com, validate_url

class SubmitURLForm(forms.Form):
    url = forms.CharField(
         label='',
         validators=[validate_url],
         widget = forms.TextInput(
                attrs={
                    "placeholder": "¿Que URL acortaremos?",
                    "class":"form-control"    
                }
            )
         )