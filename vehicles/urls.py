from django.urls import path, include
from vehicle import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('vehicles/', include('vehicle.urls')),
    path('admin/', admin.site.urls),
    #path('', views.contact),
    path('', views.add_vehicle_view),
    path('reservations', views.add_vehicle_view),
    path('maintenance', views.add_vehicle_view),
    path('vehicleAdmin', views.add_vehicle_view),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)