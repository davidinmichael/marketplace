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
        return self.get_paginated_response(serializer.data, status.HTTP_200_OK)

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
        state = State.objects.filter(country__name="Nigeria")
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


# class CreateContinent(APIView):
#     def get(self, request):
#         nigeria = Country.objects.get(name="Nigeria")
#         states = [
#             {"name": "Abia", "capital": "Umuahia"},
#             {"name": "Adamawa", "capital": "Yola"},
#             {"name": "Akwa Ibom", "capital": "Uyo"},
#             {"name": "Anambra", "capital": "Awka"},
#             {"name": "Bauchi", "capital": "Bauchi"},
#             {"name": "Bayelsa", "capital": "Yenagoa"},
#             {"name": "Benue", "capital": "Makurdi"},
#             {"name": "Borno", "capital": "Maiduguri"},
#             {"name": "Cross River", "capital": "Calabar"},
#             {"name": "Delta", "capital": "Asaba"},
#             {"name": "Ebonyi", "capital": "Abakaliki"},
#             {"name": "Edo", "capital": "Benin City"},
#             {"name": "Ekiti", "capital": "Ado Ekiti"},
#             {"name": "Enugu", "capital": "Enugu"},
#             {"name": "Gombe", "capital": "Gombe"},
#             {"name": "Imo", "capital": "Owerri"},
#             {"name": "Jigawa", "capital": "Dutse"},
#             {"name": "Kaduna", "capital": "Kaduna"},
#             {"name": "Kano", "capital": "Kano"},
#             {"name": "Katsina", "capital": "Katsina"},
#             {"name": "Kebbi", "capital": "Birnin Kebbi"},
#             {"name": "Kogi", "capital": "Lokoja"},
#             {"name": "Kwara", "capital": "Ilorin"},
#             {"name": "Lagos", "capital": "Ikeja"},
#             {"name": "Nasarawa", "capital": "Lafia"},
#             {"name": "Niger", "capital": "Minna"},
#             {"name": "Ogun", "capital": "Abeokuta"},
#             {"name": "Ondo", "capital": "Akure"},
#             {"name": "Osun", "capital": "Oshogbo"},
#             {"name": "Oyo", "capital": "Ibadan"},
#             {"name": "Plateau", "capital": "Jos"},
#             {"name": "Rivers", "capital": "Port Harcourt"},
#             {"name": "Sokoto", "capital": "Sokoto"},
#             {"name": "Taraba", "capital": "Jalingo"},
#             {"name": "Yobe", "capital": "Damaturu"},
#             {"name": "Zamfara", "capital": "Gusau"},
#             {"name": "Federal Capital Territory", "capital": "Abuja"}
#         ]

#         for state in states:
#             State.objects.create(
#                 name=state["name"], capital=state["capital"], country=nigeria)
#         return Response("Created", status.HTTP_200_OK)
