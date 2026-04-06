# local imports
from .services.crud.create import ProgramService
from .services.crud.delete import delete_program
# rest imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.db.transaction import atomic


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