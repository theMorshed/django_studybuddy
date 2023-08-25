from django.shortcuts import render
from base.models import Room

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request):
    return render(request, 'base/room.html')

def single_room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/single_room.html', context)