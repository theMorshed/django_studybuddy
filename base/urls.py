from django.urls import path
from base.views import home, room, single_room, create_room, edit_room, delete_room

urlpatterns = [
    path('', home, name='home'),
    path('room/', room),
    path('room/<str:pk>/', single_room, name='room'),
    path('create_room/', create_room, name='create_room'),
    path('edit_room/<int:pk>/', edit_room, name='edit_room'),
    path('delete_room/<int:pk>/', delete_room, name='delete_room'),
]
