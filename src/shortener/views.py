from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL
# Create your views here.

def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #Function Based View FBV
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)

class KirrCBView(View): #Class Based View CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode) 
        return HttpResponseRedirect(obj.url)

    #def post(self,request, *args, **kwargs):
    #    return HttpResponse()


'''
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #Function Based View FBV
    
    # esta es la mejor manera de las 3
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    # forma 1
    #try:
    #    obj = KirrURL.objects.get(shortcode=shortcode)
    #except:
    #    obj = KirrURL.objects.all().first()

    # forma 2 esto es mejor que el bloque try
    #obj_url = None
    #qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    #if qs.exists and qs.count() == 1:
    #    obj = qs.first()
    #    obj_url = obj.url

    return HttpResponse("Hello {sc}".format(sc=obj.url))
'''