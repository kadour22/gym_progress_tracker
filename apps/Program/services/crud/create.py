from ..ai.ai_service import AI_Service
from ...serializers import ProgramSerializer
from rest_framework.response import Response
from django.db import transaction

class ProgramService(AI_Service):
    @transaction.atomic()
    def create_program_info(self, data,user):

        serializer = ProgramSerializer(data=data)
        if serializer.is_valid():
            user_data = serializer.save(user=user)
            program_data = self.generate_gym_program(user_data=user_data)
            return {
                "user_data": ProgramSerializer(user_data).data,
                "program_data": program_data
            }
        return ({
            "error":serializer.errors
        })