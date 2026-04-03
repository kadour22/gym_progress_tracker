from rest_framework import serializers
from .models import Promgram

class ProgramSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Promgram
        fields = "__all__"