from rest_framework import serializers

class VectorSerializer(serializers.Serializer):
    numbers = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False,
        error_messages={
            'empty': 'This list may not be empty.',  
        },
        help_text="A list of integers to sum or average."
    )