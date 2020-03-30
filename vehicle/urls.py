from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import EditVehicleView, VehicleListView, AddVehicleView

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle_list'),
    path('add', AddVehicleView.as_view(), name='add_vehicle'),
    path('<int:pk>/', EditVehicleView.as_view(),name='edit_vehicle'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)