from rest_framework import serializers
from .models import Program, ProgramData

class ProgramSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Program
        fields = [

            "id",
            "age",
            "user",
            "gender",
            "progam_goal",
            "durations",
            "training",
            "height",
            "weight"

        ]

        read_only_fields = ["user","id"]

class program_serializer(serializers.ModelSerializer) :
    class Meta :
        model  = Program
        fields = ["progam_goal"] 

class ProgramDataSerializer(serializers.ModelSerializer) :
    program = program_serializer(read_only=True)
    class Meta :
        model  = ProgramData
        fields = [

            "user",
            "program",
            "data",
            "createdAt"

        ]
class DashboardSerializer(serializers.Serializer):
    programs = serializers.IntegerField()
    programs_data = serializers.IntegerField()
    consistency = serializers.IntegerField()
    progress = serializers.IntegerField()
    activity = serializers.IntegerField()