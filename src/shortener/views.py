from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #Function Based View FBV
    #print(request.user)
    #print(request.user.is_authenticated())
    #print(args)
    #print(kwargs)
    print(shortcode)
    return HttpResponse("Hello {sc}".format(sc=shortcode))

class KirrCBView(View): #Class Based View CBV
    def get(self, request, shortcode=None, *args, **kwargs): 
        return HttpResponse("Hello again {sc}".format(sc=shortcode))