from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL
from .forms import SubmitURLForm
# Create your views here.

class HomeView(View):
    

    def get(self, request, *args, **kwargs):
        form = SubmitURLForm()
        ctx = {
            "title": "Envía la URL",
            "form": form
        }
        return render(request, "shortener/home.html", ctx) 

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        ctx = {
            "title": "Envía la URL",
            "form": form
        }
        return render(request, "shortener/home.html", ctx) 

class KirrCBView(View): #Class Based View CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode) 
        print (obj.url)
        return HttpResponseRedirect(obj.url)

    def post(self,request, *args, **kwargs):
        return HttpResponse()
