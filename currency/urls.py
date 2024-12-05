from django.urls import path
from . import views

urlpatterns = [
    path("currency/", views.currency, name="currency"),

    path("currency/USD/EUR/", views.rate, name="USDEUR"),
    path("currency/EUR/USD/", views.rate, name="EURUSD"),
    path("currency/PLN/JPY/", views.rate, name="PLNJPY"),
    path("currency/JPY/EUR/", views.rate, name="JPYEUR"),
    path("currency/SEK/PLN/", views.rate, name="SEKPLN")
]
