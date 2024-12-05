from django.shortcuts import render, HttpResponse
from .models import ExchangeRate

# Create your views here.
 
def currency(request):
    # Query all currency codes form DB
    codes_from = ExchangeRate.objects.values_list("code_from")
    codes_to = ExchangeRate.objects.values_list("code_to")
    codes = codes_from.union(codes_to) # Union removes duplicates

    # Generate response from list of codes
    response = ""
    for currency in codes:
        if len(response) > 0:
            response += ", "

        response += "{\"code\":\"" + currency[0] + "\"}"

    response = "[" + response + "]"

    return HttpResponse(response)

def getCodesFromUrl(url):
    codes = url.split('/')
    return codes[2], codes[3]

def rate(request):
    # Query exchange rate from database
    code_a, code_b = getCodesFromUrl(request.get_full_path())
    exchange_rate = ExchangeRate.objects.filter(code_from = code_a, code_to = code_b).order_by("-date") # Sort by the latest

    # Generate response, if exchange rate exists in DB
    if len(exchange_rate) > 0:
        response = "{\"currency_pair\":\"" + code_a + code_b + "\", \"exchange_rate\":" + str(exchange_rate[0].rate) + "}"
        return HttpResponse(response)

    return HttpResponse("")
