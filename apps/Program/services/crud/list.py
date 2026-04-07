from ...serializers import ProgramDataSerializer, ProgramDataSerializer
from ...models import Program, ProgramData
from django.shortcuts import get_object_or_404
from rest_framework.response import Response 

class ProgramDataService:

    def list_all_program_data(self,user) :
        prog_data = ProgramData.objects.filter(program__user = user).order_by('-createdAt')
        serializer = ProgramDataSerializer(prog_data,many=True)
        return Response(serializer.data)
    
    def get_program_by_id(self,prog_id) :
        program = get_object_or_404(ProgramData, id = prog_id)
        serializer = ProgramDataSerializer(program,many=False)
        return Response(
            serializer.data
        )
    
