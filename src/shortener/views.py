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
        ctx = {
            "title": "Envía la URL",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            ctx ={
                "obj":obj,
                "created": created
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template, ctx) 

class KirrCBView(View): #Class Based View CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode) 
        print (obj.url)
        return HttpResponseRedirect(obj.url)

    def post(self,request, *args, **kwargs):
        return HttpResponse()
