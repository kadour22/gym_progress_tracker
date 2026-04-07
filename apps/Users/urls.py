from django.urls import path
from . import views


urlpatterns = [
    path("user-data/", views.UserViewService.as_view())
]