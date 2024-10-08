"""
URL configuration for config project.

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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page_view, name='home'),
    path('kits/', views.KitListView.as_view(), name='kit-list'),
    path('kits/<int:pk>/', views.KitDetailsView.as_view(), name='kit-details'),
    path('kits/search/', views.KitSearchView.as_view(), name='search'),
    path('kits/filter/', views.filter_kits_view, name='filter'),
    path("__reload__/", include("django_browser_reload.urls")),
]
