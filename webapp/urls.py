from django.urls import path
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('services/', services, name='services'),
    path('cars/', cars, name='cars'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]