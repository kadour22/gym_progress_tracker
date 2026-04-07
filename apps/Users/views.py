from .services.user_services import UserService
from rest_framework.response import Response
from rest_framework.views import APIView

class UserViewService(APIView) :

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService()
    
    def get():
        pass
    