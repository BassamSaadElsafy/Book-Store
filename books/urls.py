from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.destroy, name="destroy"),
    path("show/<int:id>", views.show, name="show"),
]