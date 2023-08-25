from django.urls import path
from base.views import home, room, single_room

urlpatterns = [
    path('', home, name='home'),
    path('room/', room),
    path('room/<str:pk>/', single_room, name='room'),
]
