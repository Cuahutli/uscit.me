from django import forms
from .validators import validate_dot_com, validate_url

class SubmitURLForm(forms.Form):
    url = forms.CharField(label='Enviar URL', validators=[validate_url, validate_dot_com])

    #esta función es para sobreescribir el comportamiento en un formulario valido .is_valid del form.cleaned_data()
    #def clean(self):
    #    cleaned_data = super(SubmitURLForm, self).clean()
    #    url = cleaned_data.get('url')
    #    print(url)
    #    url_validator = URLValidator()
    #    try:
    #        url_validator(url)
    #    except:
    #        raise forms.ValidationError("Url Invalida")
    #    return url        
    
    #esto es para limpiar un campo en particular, el metodo def clean(self) es para validar el formulario completo
    #def clean_url(self):

    #def clean_url(self):
    #    url = self.cleaned_data['url']
    #    print(url)
    #    if not "com" in url:
    #        raise forms.ValidationError("No es válida la URL por que no es una .com")
    #    return url