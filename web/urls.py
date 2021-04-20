from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path("add/", views.add, name="add"),
    path("search/", views.search, name='search'),
    path("display/", views.display, name="display"),
    path("back/", views.back, name="back"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
]
