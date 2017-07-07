from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from shortener.views import HomeView, URLRedirectView, AcercaDeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^acerca/$', AcercaDeView.as_view(), name='acerca'),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode' ),
    
]
