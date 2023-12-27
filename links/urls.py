from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<str:link_slug>/", views.root_link, name="root-link"),
    path("create/link", views.add_link, name="create-link"),
]
