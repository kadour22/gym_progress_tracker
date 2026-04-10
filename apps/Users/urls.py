from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # jwt urls
    path("get-token/", TokenObtainPairView.as_view()),
    path("refresh-token/", TokenRefreshView.as_view()),
    # urls(users)
    path("user-data/", views.UserViewService.as_view())
]