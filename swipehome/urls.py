"""swipehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from swipehomeapi.views import register_user, login_user, Users, Profile, Searches, Messages

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', Users, 'user')
router.register(r'profile', Profile, 'profile')
router.register(r'searches', Searches, 'search')
router.register(r'messages', Messages, 'messag')


urlpatterns = [
    path('', include(router.urls)),
    path('login', login_user),
    path('register', register_user),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
