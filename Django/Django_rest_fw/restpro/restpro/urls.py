from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from restapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^restpro/', views.ListEaf.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
