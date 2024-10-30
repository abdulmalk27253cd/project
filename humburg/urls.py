
from django.urls import path
from . import views
from humburg.views import humburg
urlpatterns = [
    path('humburg/', views.humburg, name='humburg')
]
