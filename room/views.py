from django.shortcuts import render


def hello(request):
    return render(request, 'room/room.html')


