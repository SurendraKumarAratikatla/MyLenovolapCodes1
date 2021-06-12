from django.contrib import admin
from django.conf.urls import url, include
from.admin import my_admin_site

urlpatterns = [
    url('admin/', admin.site.urls),
    url('ThirumalaDevasthanam/', include('ThirumalaDevasthanam.urls')),
]
