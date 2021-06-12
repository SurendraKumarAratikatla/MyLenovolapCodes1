from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class mysite(AdminSite):
    site_title = ugettext_lazy('Thirumala Devasthanam')
    site_header = ugettext_lazy('Home')
    index_title = ugettext_lazy('Thirupati')

my_admin_site = mysite()