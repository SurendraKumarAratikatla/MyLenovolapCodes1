from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from eaf import views


urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^eaf/', views.ListEaf.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)