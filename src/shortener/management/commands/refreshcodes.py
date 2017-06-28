from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL

class Command(BaseCommand):
    help = 'Refresca todos los shortcodes'

    def add_arguments(self, parser):
        #este es un parámetro obligatorio y se usa sin la leyenda Ej. python manage.py refreshcodes 10
        #parser.add_argument('items', type=int)
        
        #Esto lo convierte en parámetro opcional Ej. python manage.py refreshcodes --items 5 or python manage.py refreshcodes
        parser.add_argument('--items', type=int)
        

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes(items=options['items'])