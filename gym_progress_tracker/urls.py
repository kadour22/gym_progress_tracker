
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.Users.urls')),
    path('programs/', include('apps.Program.urls')),
    # path('accounts/', include('allauth.urls')),
]
