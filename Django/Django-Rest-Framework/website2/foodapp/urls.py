from django.urls import path

# from .views import get_api_laptop_view
from . import views

urlpatterns = [
    #path('', views.laptop_view, name = 'lap'),
    path('laptop/get/', views.get_api_laptop_view, name = 'laptop-get'),
    path('laptop/post/', views.post_api_laptop_view, name = 'laptop-post'),
]