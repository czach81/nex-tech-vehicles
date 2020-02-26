from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact),
    path('Vehicle', views.Vehicle_models_detail)
]