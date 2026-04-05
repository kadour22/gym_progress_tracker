from rest_framework import serializers
from .models import Program

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