from django.db import models

# Create your models here.

class ExchangeRate(models.Model):
    code_from = models.CharField(max_length = 3)
    code_to = models.CharField(max_length = 3)
    rate = models.DecimalField(max_digits = 10, decimal_places = 5)
    date = models.DateTimeField()
