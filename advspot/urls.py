from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='spot-home'),
    path('about/', views.about, name='spot-about'),
]
