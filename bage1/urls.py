from django.urls import path
from . import views
from bage1.views import bage1
urlpatterns = [
    path('bage1/', views.bage1, name='bage1')
]