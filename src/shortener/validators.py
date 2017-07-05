from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_validator = URLValidator()
    if not 'https://' in value:
        if not 'http://' in value:
            value = 'http://' + value
    print(value)
    try:
        url_validator(value)
    except:
        raise ValidationError("Url Invalida")
    return value        

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("No es válida la URL por que no es una .com")
    return value
