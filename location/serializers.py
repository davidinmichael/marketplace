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
    continent = serializers.SlugRelatedField(
        queryset=Continent.objects.all(), slug_field="name")
    currency = serializers.SlugRelatedField(
        queryset=Currency.objects.all(), slug_field="abbreviation")

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


class LGASerializer(serializers.ModelSerializer):
    # state = serializers.SlugRelatedField(
    #     queryset=State.objects.all(), slug_field="name")
    class Meta:
        model = LGA
        fields = ["name"]

    def validate_state(self, value):
        try:
            state = State.objects.get(name=value)
        except State.DoesNotExist:
            raise serializers.ValidationError({"message": "Invalid State"})
        return value


class StateSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(
        queryset=Country.objects.all(), slug_field="name")
    lgas = LGASerializer(many=True, read_only=True, source="lga_set")

    class Meta:
        model = State
        fields = ["id", "name", "capital", "country", "lgas"]

    extra_kwargs = {
        "id": {"read_only": True}
    }

    def validate_country(self, value):
        try:
            country = Country.objects.get(name=value)
        except Country.DoesNotExist:
            raise serializers.ValidationError({"message": "Invalid Country"})
        return value

    def to_representation(self, instance):
        ret = super(StateSerializer, self).to_representation(instance)
        ret["lgas"] = [lga_data["name"] for lga_data in ret["lgas"]]
        return ret


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
