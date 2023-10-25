from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} | {self.abbreviation}"


class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    capital = models.CharField(max_length=100, unique=True)
    currency = models.ForeignKey(
        Currency, blank=True, null=True, on_delete=models.SET_NULL)
    continent = models.ForeignKey(
        Continent, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} | {self.capital}"


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capital = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} | {self.capital}"


class LGA(models.Model):
    name = models.CharField(max_length=100, unique=True)
    state = models.ForeignKey(State, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.state}"


class Address(models.Model):
    address = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    lga = models.ForeignKey(LGA, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(State, null=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.town} | {self.state}, {self.country}"
