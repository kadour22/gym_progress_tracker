from django.urls import path
from . import views

urlpatterns = [
    path("ai-generate-program/", views.GenerateProgramView.as_view()),
    path("program/<int:program_id>/", views.DeleteProgramView.as_view()),
]