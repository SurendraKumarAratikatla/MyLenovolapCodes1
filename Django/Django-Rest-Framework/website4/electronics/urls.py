from django.urls import path

# from .views import get_api_laptop_view
from . import views

urlpatterns = [
    #path('', views.laptop_view, name = 'lap'),
    path('laptop/get/', views.get_api_laptop_view, name = 'laptop-get'),
    path('laptop/get-detail/<str:pk>/', views.get_detail_api_laptop_view, name = 'laptop-get-detail'),
    path('laptop/update/<str:pk>/', views.update_api_laptop_view, name = 'laptop-post'),
    path('laptop/delete/<str:pk>/', views.delete_api_laptop_view, name = 'laptop-delete'),
    path('laptop/create/', views.create_api_laptop_view, name = 'laptop-create'),
    path('register/', views.registration_api, name = 'register'),
]