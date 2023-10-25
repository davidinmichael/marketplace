from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class ContinentAddList(APIView):
    def get(self, request):
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = ContinentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Continent Created Successfully",
                             "continent": serializer.data}, status.HTTP_201_CREATED)
        return Response({"message": "Error creating continent",
                         "errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)


class CurrencyAddList(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        if currencies is None:
            return Response({"message": "No currency found."}, status.HTTP_404_NOT_FOUND)
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Currency Created Successfully",
                             "currency": serializer.data}, status.HTTP_201_CREATED)
        return Response({"message": "Error creating currency",
                         "errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)
