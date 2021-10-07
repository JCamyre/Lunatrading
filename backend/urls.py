"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers
from stocks import views
from .views import index
from django.conf import settings
from django.conf.urls.static import static
from social_login.views import FacebookLogin, GoogleLogin

router = routers.DefaultRouter()
router.register(r'stocks', views.StocksView, 'stock')
# We can now do /stats/ to access all stat objects, and we can perform create and read
# /stats/id can do update and delete on a specific object. Idk what 'stock' does.
# CRUD

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('stocks/', include('stocks.urls')),  # Is it better to name this api/?
    path('api/v1/users/', include('users.urls'))
]

# I should redesign how the backend server does calculations. Better url names, etc.
