from django.http import HttpResponse

def index(response):
    return HttpResponse("<h2>This is Music App</h2>")

def __str__(self):
    return self.album_title + '-' + self.artist
