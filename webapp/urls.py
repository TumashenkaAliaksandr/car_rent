from django.urls import path
from django.conf.urls.static import static
from car_rent import settings
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('services/', services, name='services'),
    path('cars/', cars, name='cars'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)