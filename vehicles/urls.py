from django.urls import path, include
from vehicle import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from vehicle.views import VehicleListView

urlpatterns = [
    path('vehicles/', include('vehicle.urls')),
    path('maintenance/', include('maintenance.urls')),
    path('admin/', admin.site.urls),
    path('', VehicleListView.as_view()),
    path('reservations', VehicleListView.as_view()),
    path('vehicleAdmin', VehicleListView.as_view()),
    

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)