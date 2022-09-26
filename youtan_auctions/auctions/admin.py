from django.contrib import admin

from .models import Auction, Property, Vehicle

admin.site.register(Auction)
admin.site.register(Property)
admin.site.register(Vehicle)
