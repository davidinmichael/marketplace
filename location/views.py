from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *


class ContinentList(APIView):
    def get(self, request):
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class CurrencyAddList(APIView, PageNumberPagination):
    def get(self, request):
        currencies = Currency.objects.all()
        if currencies is None:
            return Response({"message": "No currency found."}, status.HTTP_404_NOT_FOUND)
        response = self.paginate_queryset(currencies, request, view=self)
        serializer = CurrencySerializer(response, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Currency Created Successfully",
                             "currency": serializer.data}, status.HTTP_201_CREATED)
        return Response({"message": "Error creating currency",
                         "errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)


class CountryAddList(APIView, PageNumberPagination):
    def get(self, request):
        countries = Country.objects.all()
        if countries is None:
            return Response({"message": "No countries found."}, status.HTTP_404_NOT_FOUND)
        response = self.paginate_queryset(countries, request, view=self)
        serializer = CountrySerializer(response, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Country Created Successfully",
                             "country": serializer.data}, status.HTTP_201_CREATED)
        return Response({"message": "Error creating country",
                         "errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)


class StateList(APIView):
    def get(self, request):
        state = State.objects.filter(country__name="Nigeria").order_by("name")
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class SingleState(APIView):
    def get(self, request, pk):
        state = State.objects.get(id=pk)
        serializer = StateSerializer(state)
        return Response(serializer.data, status.HTTP_200_OK)


# class CreateLocation(APIView):
#     def get(self, request):
#         abia = State.objects.get(name="Zamfara")
#         states = [
#             "Anka",
#             "Bakura",
#             "Birnin Magaji/Kiyaw",
#             "Bukkuyum",
#             "Gummi",
#             "Gusau",
#             "Kaura Namoda",
#             "Maradun",
#             "Maru",
#             "Shinkafi",
#             "Talata Mafara",
#             "Zurmi"
#         ]

#         for i in range(len(states)):
#             LGA.objects.create(name=states[i], state=abia)
#         return Response("Created", status.HTTP_200_OK)
