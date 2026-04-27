from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('services/', include('services.urls')),
    path('admin-panel/', include('adminpanel.urls')),
    path('', RedirectView.as_view(url='/services/dashboard/', permanent=False)),
]
