from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

# from .views import get_api_laptop_view
from . import views

urlpatterns = [
    path('register/', views.registration_api, name = 'register'),
    path('login/', obtain_auth_token, name = 'login')
]