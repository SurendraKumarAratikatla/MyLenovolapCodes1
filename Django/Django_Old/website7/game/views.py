from django.http import HttpResponse
from django.shortcuts import render
from .models import game

def index(request):
    all_games = game.objects.all()
    context = {
        'all_games' : all_games
    }
    return render(request,'game/index.html',context)

def gameview(response):
    return HttpResponse("<h1>Ludo King</h1>")


