from django.contrib import admin
from .models import ExchangeRate

# Register your models here.

class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('code_from', 'code_to', 'rate', 'date')
    list_filter = ['code_from', 'code_to']
    search_fields = ['code_from', 'code_to']

admin.site.register(ExchangeRate, ExchangeRateAdmin)
