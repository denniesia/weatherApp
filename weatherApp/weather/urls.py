from django.urls import path
from weatherApp.weather import views

urlpatterns = [
    path('', views.home, name='home'),
]