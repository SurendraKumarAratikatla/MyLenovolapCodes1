from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^game/',include('game.urls')),
    url(r'^ludo/',include('game.urls'))
]
