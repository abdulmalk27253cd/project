
from django.urls import path
from . import views
from bage2.views import bage2
urlpatterns = [
    path('bage2/', views.bage2, name='bage2')
]
