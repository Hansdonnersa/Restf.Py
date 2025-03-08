from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VectorSerializer

class SumView(APIView):
    def post(self, request):
        serializer = VectorSerializer(data=request.data)
        if serializer.is_valid():
            numbers = serializer.validated_data['numbers']
            total = sum(numbers)
            return Response({'sum': total}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AverageView(APIView):
    def post(self, request):
        serializer = VectorSerializer(data=request.data)
        if serializer.is_valid():
            numbers = serializer.validated_data['numbers']
            average = sum(numbers) / len(numbers)
            return Response({'average': average}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
