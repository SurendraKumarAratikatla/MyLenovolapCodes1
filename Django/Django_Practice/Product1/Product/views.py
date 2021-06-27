from django.http import HttpResponse

def index(requst):
    return HttpResponse("<h2>Hello World<h2>")
