from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def kirr_redirect_view(request): #Function Based View FBV
    return HttpResponse("Hello")

class KirrCBView(View): #Class Based View CBV
    def get(self, request, *args, **kwargs): 
        return HttpResponse("hellos Again")