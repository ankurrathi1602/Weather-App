from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('base.html', views.base, name="base"),

]