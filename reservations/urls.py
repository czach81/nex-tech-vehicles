from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import MakeReservationView, MyReservationView, DetailReservationView, ReservationWizard
from .forms import MakeReservationForm, DetailReservationForm, SelectVehicleReservationForm

reservation_form_list = [MakeReservationForm, SelectVehicleReservationForm, DetailReservationForm]

urlpatterns = [
    #path('<int:pk>/', VehicleMaintenanceListView.as_view(),name='maintenance_list'),
    path('add', ReservationWizard.as_view(reservation_form_list), name='new_reservation'),
    path('', MyReservationView.as_view(), name='reservations'),
    #path('<int:vehicle_pk>/mileage/add', AddMileageView.as_view(), name='add_mileage'),
    #path('', VehicleMaintenanceListView.as_view(),name='maintenance'),
    #path('', VehicleListView.as_view(), name='vehicle_list'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)