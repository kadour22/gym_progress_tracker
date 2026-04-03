from .serializers import ProgramSerializer
from .models import Promgram

from rest_framework.views import APIView
from rest_framework.response import Response


# class my_view(APIView) :

#     def post(self, request) :

#         serializer = ProgramSerializer(data=request.data)
#         if serializer.is_valid() :

#             generate_program = serializer.save()
