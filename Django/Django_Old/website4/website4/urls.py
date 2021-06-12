from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('Stocks/', views.StockList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)