from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),

    path('task-listcomm/', views.taskListComm, name='task-listcomm'),
    path('task-detailcomm/<str:pk>/', views.taskDetailComm, name='task-detailcomm'),
    path('task-createcomm/', views.taskCreateComm, name='task-createcomm'),
    path('task-updatecomm/<str:pk>/', views.taskUpdateComm, name='task-updatecomm'),
    path('task-deletecomm/<str:pk>/', views.taskDeleteComm, name='task-deletecomm'),
]