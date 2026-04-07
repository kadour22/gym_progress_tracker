from django.urls import path
from . import views

urlpatterns = [
    path("ai-generate-program/", views.GenerateProgramView.as_view()),
    path("program/<int:program_id>/", views.DeleteProgramView.as_view()),

    path("program-data/", views.ProgramDataView.as_view()),
    path("program-data/program/<int:prog_id>/", views.ProgramDataView.as_view()),
    
]