from django.urls import path, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from shortener.views import HomeView, URLRedirectView, AcercaDeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('acerca/', AcercaDeView.as_view(), name='acerca'),
    re_path(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode' ),
    
]


if settings.DEBUG == False:
    # static files (images, css, javascript, etc.)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)