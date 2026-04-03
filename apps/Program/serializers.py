from rest_framework import serializers
from .models import Promgram

class ProgramSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Promgram
        fields = [
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