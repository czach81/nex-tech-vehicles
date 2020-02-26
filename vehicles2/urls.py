
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('vehicle/', include('vehicle.urls')),
    path('admin/', admin.site.urls),
]
