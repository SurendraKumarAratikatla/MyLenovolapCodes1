from django.contrib import admin
from .models import ChemicalElement, Commodity

admin.site.register(ChemicalElement)
admin.site.register(Commodity)