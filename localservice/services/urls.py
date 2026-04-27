from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/', views.user_dashboard, name='user_dashboard'),
    path('worker/', views.worker_dashboard, name='worker_dashboard'),
    path('accept/<int:pk>/', views.accept_request, name='accept_request'),
    path('reject/<int:pk>/', views.reject_request, name='reject_request'),
    path('complete/<int:pk>/', views.complete_request, name='complete_request'),
]
