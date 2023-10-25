from django.urls import path
from .views import *


urlpatterns = [
    path("create/", CreateLocation.as_view()),
    path("continents/", ContinentList.as_view()),
    path("countries/", CountryAddList.as_view()),
    path("states/", StateList.as_view()),
    path("state/<str:pk>/", SingleState.as_view()),
    path("currencies/", CurrencyAddList.as_view()),
]
