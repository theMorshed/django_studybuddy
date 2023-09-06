from django.shortcuts import render, redirect
from base.models import Room
from base.forms import RoomForm

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

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {'form': form}
    return render(request, 'base/create_room.html', context)