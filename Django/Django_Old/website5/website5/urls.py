from django.contrib import admin
from django.conf.urls import url
from.admin import my_admin_site

urlpatterns = [
    url('admin/', my_admin_site.urls),
]
