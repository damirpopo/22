from grud import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index),
    path("create", views.create),
    path("edit/<int:id>", views.edit),
    path("delete/<int:id>", views.delete),
    path('admin/', admin.site.urls),
]
