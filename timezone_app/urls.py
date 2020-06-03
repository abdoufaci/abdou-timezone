from django.urls import path
from . import views

urlpatterns = [
    path('timezone_search', views.timezone_search, name='timezone_search'),
    path('', views.home, name='home'),
]