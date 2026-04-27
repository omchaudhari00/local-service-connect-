from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('delete/<int:pk>/', views.delete_request, name='delete_request'),
]
