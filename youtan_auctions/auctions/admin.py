from django.contrib import admin

from .models import Auction, Bank, Property, Vehicle

admin.site.register(Auction)
admin.site.register(Bank)
admin.site.register(Property)
admin.site.register(Vehicle)
