from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitURLForm
from .models import KirrURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitURLForm()
        ctx = {
            "title": "uscit.me",
            "form": form
        }
        return render(request, "shortener/home.html", ctx) 

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        ctx = {
            "title": "uscit.me",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            if not 'https://' in new_url:
                if not 'http://' in new_url:
                    new_url = 'http://' + new_url
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

class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        return HttpResponseRedirect(obj.url)


class AcercaDeView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return render(request, 'acerca.html',{})