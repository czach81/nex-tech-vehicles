from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import VehicleMaintenanceListView, AddMaintenanceView, MaintenanceDetailView, AddMileageView 

urlpatterns = [
    path('<int:pk>/', VehicleMaintenanceListView.as_view(),name='maintenance_list'),
    path('<int:vehicle_pk>/maintenance/add', AddMaintenanceView.as_view(), name='add_maintenance'),
    path('<int:vehicle_pk>/maintenance', MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('<int:vehicle_pk>/mileage/add', AddMileageView.as_view(), name='add_mileage'),
    path('', VehicleMaintenanceListView.as_view(),name='maintenance'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)