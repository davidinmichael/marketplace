from rest_framework import serializers
from .models import *


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ["name", "abbreviation"]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"

    extra_kwargs = {
        "id": {"read_only": True}
    }


class CountrySerializer(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(queryset=Currency.objects.all(), slug_field="name")
    continent = serializers.SlugRelatedField(queryset=Continent.objects.all(), slug_field="name")
    class Meta:
        model = Country
        fields = "__all__"

    extra_kwargs = {
        "id": {"read_only": True}
    }

    # def validate_currency(self, value):
    #     try:
    #         currency = Currency.objects.get(abbreviation=value)
    #     except Currency.DoesNotExist:
    #         raise serializers.ValidationError({"message": "Invalid currency"})
    #     return value

    def validate_continent(self, value):
        try:
            continent = Continent.objects.get(name=value)
        except Continent.DoesNotExist:
            raise serializers.ValidationError(
                {"message": "Invalid continent"})
        return value


class StateSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field="name")
    class Meta:
        model = State
        fields = "__all__"

    extra_kwargs = {
        "id": {"read_only": True}
    }

    def validate_country(self, value):
        try:
            country = Country.objects.get(name=value)
        except Country.DoesNotExist:
            raise serializers.ValidationError({"message": "Invalid Country"})
        return value


class LGASerializer(serializers.ModelSerializer):

    class Meta:
        model = LGA
        fields = ["name", "state"]

    def validate_state(self, value):
        try:
            state = State.objects.get(name=value)
        except State.DoesNotExist:
            raise serializers.ValidationError({"message": "Invalid State"})
        return value


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    extra_kwargs = {
        "id": {"read_only": True}
    }

    def validate_lga(self, value):
        try:
            lga = LGA.objects.get(name=value)
        except LGA.DoesNotExist:
            raise serializers.ValidationError({"message": "Invalid LGA"})
        return value

    def validate_state(self, value):
        try:
            state = State.objects.get(name=value)
        except State.DoesNotExist:
            raise serializers.ValidationError({"message": "Invalid State"})
        return value

    def validate_country(self, value):
        try:
            country = Country.objects.get(name=value)
        except Country.DoesNotExist:
            raise serializers.ValidationError({"message": "Invalid Country"})
        return value
