from django.contrib import admin
from .models import Vehicle, Maintenance, Mileage

admin.site.register(Vehicle)
admin.site.register(Maintenance)
admin.site.register(Mileage)
