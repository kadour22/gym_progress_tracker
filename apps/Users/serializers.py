from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    programs_data = serializers.IntegerField()
    programs = serializers.IntegerField()