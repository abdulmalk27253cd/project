
from django.urls import path
from . import views
from search.views import search_product
urlpatterns = [
    path('search/', views.search_product, name='search_product')
]
