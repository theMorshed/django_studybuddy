from django.urls import path
from base.views import home, room

urlpatterns = [
    path('', home, name='home'),
    path('room/', room, name='room'),
]
