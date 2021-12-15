from django.shortcuts import render
import threading
# Create your views here.

def homepage(request):
    print(threading.get_native_id())
    return render(request, 'chat_app/index.html')

def room(request, room_name):
    context = {
        'room_name': room_name,
    }
    return render(request, 'chat_app/room.html', context)
