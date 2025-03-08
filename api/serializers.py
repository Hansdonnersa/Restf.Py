from rest_framework import serializers

class VectorSerializer(serializers.Serializer):
    numbers = serializers.ListField(child=serializers.IntegerField())