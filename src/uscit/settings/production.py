from .base import * 
''' a partir de aqui irá en archivos separados para producción y local '''
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['uscit.me', 'www.uscit.me']

ROOT_HOSTCONF = 'uscit.hosts'
DEFAULT_HOST = 'www'
DEFAULT_REDIRECT_URL = 'http://www.uscit.me'
PARENT_HOST = 'uscit.me'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


