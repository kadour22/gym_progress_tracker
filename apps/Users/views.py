from .services.user_services import UserService
from ..Program.serializers import ProgramDataSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer


class UserViewService(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService()

    def get(self, request):
        service = self.user_service
        programs = service.get_user_programs(request.user)
        programs_data = service.get_user_program_data(request.user).count()

        data = {
            "programs": programs,
            "programs_data": programs_data
        }

        serializer = UserSerializer(data)
        return Response(serializer.data)
    
    