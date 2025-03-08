from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VectorSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class SumView(APIView):
    """
    Endpoint to sum a list of integers.

    Example request:
    ```json
    {
        "numbers": [1, 2, 3, 4, 5]
    }
    ```

    Example response:
    ```json
    {
        "sum": 15
    }
    """
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'numbers': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_INTEGER),
                    example=[1, 2, 3, 4, 5],  # Exemplo pré-preenchido
                ),
            },
            required=['numbers'],
        ),
        responses={
            200: openapi.Response(
                description="The sum of the numbers.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'sum': openapi.Schema(type=openapi.TYPE_INTEGER, example=15),
                    },
                ),
            ),
            400: openapi.Response(
                description="Invalid input.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'numbers': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
                    },
                ),
            ),
        },
    )
    def post(self, request):
        """
        Sum a list of integers.

        Example request:
        ```json
        {
            "numbers": [1, 2, 3, 4, 5]
        }
        ```

        Example response:
        ```json
        {
            "sum": 15
        }
        """
        serializer = VectorSerializer(data=request.data)
        if serializer.is_valid():
            numbers = serializer.validated_data['numbers']
            if len(numbers) == 0:  # Verifica se a lista está vazia
                return Response({'numbers': ['This list may not be empty.']}, status=status.HTTP_400_BAD_REQUEST)
            total = sum(numbers)
            return Response({'sum': total}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AverageView(APIView):
    """
    Endpoint to calculate the average of a list of integers.

    Example request:
    ```json
    {
        "numbers": [10, 20, 30, 40, 50]
    }
    ```

    Example response:
    ```json
    {
        "average": 30
    }
    """
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'numbers': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_INTEGER),
                    example=[10, 20, 30, 40, 50],  # Exemplo pré-preenchido
                ),
            },
            required=['numbers'],
        ),
        responses={
            200: openapi.Response(
                description="The average of the numbers.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'average': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, example=30.0),
                    },
                ),
            ),
            400: openapi.Response(
                description="Invalid input.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'numbers': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
                    },
                ),
            ),
        },
    )
    def post(self, request):
        """
        Calculate the average of a list of integers.

        Example request:
        ```json
        {
            "numbers": [10, 20, 30, 40, 50]
        }
        ```

        Example response:
        ```json
        {
            "average": 30.0
        }
        """
        serializer = VectorSerializer(data=request.data)
        if serializer.is_valid():
            numbers = serializer.validated_data['numbers']
            if len(numbers) == 0:  # Verifica se a lista está vazia
                return Response({'numbers': ['This list may not be empty.']}, status=status.HTTP_400_BAD_REQUEST)
            average = sum(numbers) / len(numbers)
            return Response({'average': average}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
