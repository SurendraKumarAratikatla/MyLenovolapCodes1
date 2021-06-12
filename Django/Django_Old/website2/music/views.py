from django.http import HttpResponse
from .models import Album
#from django.template import loader
from django.shortcuts import render


def index(response):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    context = {'all_albums':all_albums,}
    return render(response,'music/index.html',context)

def detail(response, album_id):
    return HttpResponse("<h2>Details for Album id : "+ str(album_id) +"</h2>")

