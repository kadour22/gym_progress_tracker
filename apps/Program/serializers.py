from rest_framework import serializers
from .models import Program, ProgramData

class ProgramSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Program
        fields = [
            "id",
            "user",
            "age",
            "gender",
            "progam_goal",
            "durations",
            "training",
            "height",
            "weight"
        ]

        read_only_fields = ["user"]

class program_serializer(serializers.ModelSerializer) :
    class Meta :
        model  = Program
        fields = ["progam_goal"] 

class ProgramDataSerializer(serializers.ModelSerializer) :
    program = program_serializer(read_only=True)
    class Meta :
        model  = ProgramData
        fields = [
            "user","program","data","createdAt"
        ]