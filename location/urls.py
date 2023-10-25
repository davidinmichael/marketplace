from django.urls import path
from .views import *


urlpatterns = [
    path("continents/", ContinentList.as_view()),
    path("countries/", CountryAddList.as_view()),
    path("states/", StateList.as_view()),
]
