from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('analyze/', views.analyze, name="analyze"),
    path('network/', views.network_request, name="net_req")
]
