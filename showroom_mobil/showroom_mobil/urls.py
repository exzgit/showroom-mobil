"""
URL configuration for showroom_mobil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.dashboard, name="dashboard"),
    path('dashboard/', index.dashboard, name="dashboard"),
    path('add_car/', index.add_car, name="add_car"),
    path('edit_car/<int:id>', index.edit_car, name="edit_car"),
    path('delete_car/<int:id>', index.delete_car, name="delete_car"),
    path('detail_car/<int:id>', index.detail_car, name="detail_car"),

    path('add_service/<int:id>', index.add_service, name="add_service"),
    path('detail_car/edit_service/<int:id>', index.edit_service, name="edit_service"),
    path('delete_service/<int:id>', index.delete_service, name="delete_service"),
]
