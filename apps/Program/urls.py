from django.urls import path
from . import views


urlpatterns = [
    path("ai-generate-program/", views.GenerateProgramView.as_view()),
]