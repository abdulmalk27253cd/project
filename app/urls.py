"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.generic.base import TemplateView
from app.views import index
from search.views import search
# from login.views import registration
# from search.views import searh
# from signup.views import signup
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
 path('admin/', admin.site.urls),
 path('', home, name='index'),
 path("registration/",  include("django.contrib.auth.urls")),
 path("accounts/", include("accounts.urls")),
 path("login/", views.login_user, name='login'),
 path("logout/", views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)