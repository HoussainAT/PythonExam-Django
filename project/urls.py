"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from factureapp.views import home_page, add_facture, delete_facture, update_facture

urlpatterns = [
    path('', home_page),
    path('add_facture/',add_facture),
    path('admin/', admin.site.urls),
    path('delete_facture/<int:id>', delete_facture),
    path('update_facture/<int:id>/', update_facture)
]
