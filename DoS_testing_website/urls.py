from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    #
    path("", views.home, name="home"),
    #
    path("bw", views.bwHome, name="bwHome"),
    #
    path("cpu", views.cpuHome, name="cpuHome"),
    #
    path("ram", views.ramHome, name="ramHome"),
]