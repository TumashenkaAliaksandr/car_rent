from django.urls import path
from django.conf.urls.static import static
from car_rent import settings
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('cars/', CarListView.as_view(), name='cars'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),

    path('accounts/login/', CRLoginView.as_view(), name='login'),
    path('accounts/logout/', CRLogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/regitster/done/', RegisterDoneView.as_view(), name='register_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)