"""
URL configuration for final_project project.

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
from django.urls import path

from tvshows.views import index, shows, tvshow_create, tvshow_update, tvshow_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('tvshows/', shows, name='tvshows'),
    path('create/', tvshow_create, name='tvshow_create'),
    path('update/<int:pk>/', tvshow_update, name='tvshow_update'),
    path('delete/<int:pk>/', tvshow_delete, name='tvshow_delete'),
]
