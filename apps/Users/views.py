
from rest_framework.views import APIView
from rest_framework.response import Response


class test_view(APIView) :

    def get(self, request) :
        return Response("hello")