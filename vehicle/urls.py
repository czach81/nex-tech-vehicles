from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import EditVehicleView, VehicleListView

urlpatterns = [
    path('', VehicleListView.as_view()),
    path('add', views.add_vehicle_view),
    path('<int:id>/', EditVehicleView.as_view()),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)