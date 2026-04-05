# local imports
from .services.crud.create import ProgramService
# rest imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

class GenerateProgramView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        program_service = ProgramService()
        result = program_service.create_program_info(data=request.data,user=request.user)
        if "errors" in result:
            return Response(result["errors"], status=400)
        return Response(result, status=201)
