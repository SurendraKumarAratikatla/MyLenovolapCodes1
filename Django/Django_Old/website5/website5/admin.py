from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class mysite(AdminSite):
    site_title = ugettext_lazy('Jio-Savan')
    site_header = ugettext_lazy('Home')
    index_title = ugettext_lazy('JIO')

my_admin_site = mysite()
