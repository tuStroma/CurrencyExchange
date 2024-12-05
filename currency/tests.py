from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import *

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_currency_url_resolves_correctly(self):
        url = reverse("currency")
        self.assertEqual(resolve(url).func, currency)
        
    def test_USD_EUR_url_resolves_correctly(self):
        url = reverse("USDEUR")
        self.assertEqual(resolve(url).func, rate)
        
    def test_EUR_USD_url_resolves_correctly(self):
        url = reverse("EURUSD") 
        self.assertEqual(resolve(url).func, rate)

    def test_PLN_JPY_url_resolves_correctly(self):
        url = reverse("PLNJPY") 
        self.assertEqual(resolve(url).func, rate)

    def test_JPY_EUR_url_resolves_correctly(self):
        url = reverse("JPYEUR") 
        self.assertEqual(resolve(url).func, rate)

    def test_SEK_PLN_url_resolves_correctly(self):
        url = reverse("SEKPLN") 
        self.assertEqual(resolve(url).func, rate)
