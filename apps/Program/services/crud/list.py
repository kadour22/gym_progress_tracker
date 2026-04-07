from ...serializers import ProgramDataSerializer, ProgramDataSerializer
from ...models import Program, ProgramData
from django.shortcuts import get_object_or_404
from rest_framework.response import Response 

class ProgramDataService:

    def list_all_program_data(self, user):
        return ProgramData.objects.filter(user=user).order_by('-createdAt')

    def get_program_by_id(self, prog_id):
        return get_object_or_404(ProgramData, id=prog_id)