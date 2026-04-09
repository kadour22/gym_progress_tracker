# local imports
from .services.crud.create import ProgramService
from .services.crud.delete import delete_program
from .services.crud.list import ProgramDataService
# rest imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.db.transaction import atomic
from .permissions.permissions import IsProgramOwner
from .serializers import ProgramDataSerializer,ProgramSerializer
from rest_framework.response import Response

class GenerateProgramView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        program_service = ProgramService()
        result = program_service.create_program_info(data=request.data,user=request.user)
        if "errors" in result:
            return Response(result["errors"], status=400)
        return Response(result, status=201)

class DeleteProgramView(APIView) :
    permission_classes = [permissions.IsAuthenticated]
    def delete(self,program_id) :
        return delete_program(program_id=program_id)

class ProgramDataView(APIView) :
    permission_classes = [permissions.IsAuthenticated]
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.program_data_service = ProgramDataService()
    def get(self, request) :
        program = self.program_data_service.list_all_program_data(user=request.user)
        serializer = ProgramDataSerializer(program,many=True)
        return Response(serializer.data) 
    
class SingleProgramData(APIView):
    permission_classes = [IsProgramOwner]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.program_data_service = ProgramDataService()

    def get(self, request, program_id):
        program = self.program_data_service.get_program_by_id(program_id)
        self.check_object_permissions(request, program)
        serializer = ProgramDataSerializer(program)
        return Response(serializer.data)
