
from django.urls import path
from .views import index, about, doctor, service, contact, home, map

urlpatterns = [
    path('', index, name='index' ),
    path('doctor', doctor, name='doctor' ),
    path('homepage', home, name='homepage' ),
    path('service', service, name='service' ),
    path('contact', contact, name='contact' ),
    path('about', about, name='about' ),
    path('map', map, name='map' )
]
