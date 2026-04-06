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

class ProgramDataSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = ProgramData
        fields = [
            "program","data","creratedAt"
        ]