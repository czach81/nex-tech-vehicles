from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import EditVehicleView, VehicleListView, AddVehicleView, VehicleMaintenanceListView, AddMaintenanceView, MaintenanceDetailView, AddMileageView 

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle_list'),
    path('add', AddVehicleView.as_view(), name='add_vehicle'),
    path('<int:pk>/', EditVehicleView.as_view(),name='edit_vehicle'),
    path('<int:pk>/', VehicleMaintenanceListView.as_view(),name='maintenance'),
    path('<int:vehicle_pk>/maintenance/add', AddMaintenanceView.as_view(), name='add_maintenance'),
    path('<int:vehicle_pk>/maintenance', MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('<int:vehicle_pk>/mileage/add', AddMileageView.as_view(), name='add_mileage'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)