from django.shortcuts import render

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Javascript es6 learning'},
    {'id': 3, 'name': 'Discuss with PHP'},
    {'id': 4, 'name': 'Hello Universe'},
]
def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request):
    return render(request, 'base/room.html')

def single_room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/single_room.html', context)