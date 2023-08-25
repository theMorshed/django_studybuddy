from django.shortcuts import render

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Javascript es6 learning'},
    {'id': 3, 'name': 'Discuss with PHP'},
    {'id': 4, 'name': 'Hello Universe'},
]
def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')