from django.contrib import admin

from .models import Auction, Bank, Property, PropertyImages, Vehicle

admin.site.register(Auction)
admin.site.register(Bank)
admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(Vehicle)
