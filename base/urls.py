from django.urls import path
from base.views import home, room, single_room, create_room

urlpatterns = [
    path('', home, name='home'),
    path('room/', room),
    path('room/<str:pk>/', single_room, name='room'),
    path('create_room/', create_room, name='create_room'),
]
