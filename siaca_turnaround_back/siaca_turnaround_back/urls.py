"""
URL configuration for siaca_turnaround_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('vuelos/', include('api.vuelos.api.urls')),
    path('plantillas/', include('api.plantillas.api.urls')),
    path('usuarios/', include('api.usuarios.api.urls')),
    path('aerolineas/', include('api.aerolineas.api.urls')),
    path('turnarounds/', include('api.turnarounds.api.urls')),
    path('maquinarias/', include('api.maquinarias.api.urls')),
    path('documentos/', include('api.documentos.api.urls')),
    path('metricas/', include('api.metricas.api.urls')), 
    
]
