from django.urls import path

# from .views import api_laptop_view
from . import views

urlpatterns = [
    #path('', views.laptop_view, name = 'lap'),
    path('laptop/', views.api_laptop_view, name = 'lapapi'),
]