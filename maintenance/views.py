from django.views.generic import FormView, CreateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MaintenanceForm, MileageForm
from maintenance.models import  Maintenance, Mileage
from vehicle.models import Vehicle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.db.models import Max, OuterRef, Subquery




    
class MaintenanceDetailView(CreateView):
    form_class = MaintenanceForm
    template_name = "view_maintenance.html"
    
    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        elif self.request.method == 'GET':
            kwargs.update({
                'data': self.request.GET.copy()
            })
        return kwargs 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle_pk = self.kwargs.get('vehicle_pk')
        vehicle = Vehicle.objects.get(id=vehicle_pk)
        maintenance_notes = vehicle.maintenance.all()
         # start here to be able to read get request query parameters for django 
        status = self.request.GET.get('status')
        if status == 'ACTIVE':
            queryset = queryset.filter(active = True)
        elif status == 'NONACTIVE':
            queryset = queryset.filter(active = False)

        paginator = Paginator(maintenance_notes, 10)

        page = self.request.GET.get('page')
        try:
          queryset = paginator.page(page)
        except PageNotAnInteger:
          queryset = paginator.page(1)
        except EmptyPage:
          queryset = paginator.page(paginator.num_pages)

        context.update({
        "maintenance_list": queryset,
        "vehicle": vehicle,
        "title": "List"
        })

        return context




class AddMaintenanceView(CreateView):
    form_class = MaintenanceForm
    template_name = "add_maintenance.html"
    model = Maintenance

    def get_success_url(self):
        from django.urls import reverse
        return reverse('maintenance_list', kwargs={'pk':self.kwargs.get('vehicle_pk')}) 

    def get_initial(self):
        return {'vehicle': self.kwargs.get('vehicle_pk')}

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class AddMileageView(CreateView):
    form_class = MileageForm
    template_name = "add_mileage.html"
    model = Mileage

    def get_initial(self):
        return {'vehicle': self.kwargs.get('vehicle_pk')}
    

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    

    def get_success_url(self):
        from django.urls import reverse
        return reverse('maintenance') 

class VehicleMaintenanceListView(FormView):
    form_class = MaintenanceForm #new form goes here for status 
    template_name = "maintenance.html"
    
    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        elif self.request.method == 'GET':
            kwargs.update({
                'data': self.request.GET.copy()
            })
        return kwargs 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Vehicle.objects.filter(
                active=True
            ).annotate(
                latest_mileage=Subquery(
                    Mileage.objects.filter(
                        vehicle_id=OuterRef('id')
                    ).order_by(
                        '-month', '-year'
                    ).values(
                        'month_End_Mileage',
                    )[:1]
                ),
                latest_changed_Oil=Subquery(
                    Maintenance.objects.filter(
                        changed_Oil=True,
                        vehicle_id=OuterRef('id')
                    ).order_by(
                        '-maintenance_Date'
                    ).values(
                        'maintenance_Date'
                    )[:1]
                ),
                latest_month=Subquery(
                    Mileage.objects.filter(
                
                        vehicle_id=OuterRef('id')
                    ).order_by(
                        '-month', '-year'
                    ).values(
                        'month'
                    )[:1]
                ),
                latest_year=Subquery(
                    Mileage.objects.filter(
                        vehicle_id=OuterRef('id')
                    ).order_by(
                        '-month', '-year'
                    ).values(
                        'year', 
                    )[:1]
                )
            ).order_by('vehicle_Number')
            

        paginator = Paginator(queryset, 5)

        page = self.request.GET.get('page')
        try:
          queryset = paginator.page(page)
        except PageNotAnInteger:
          queryset = paginator.page(1)
        except EmptyPage:
          queryset = paginator.page(paginator.num_pages)

        context.update({
        "vehicle_list": queryset,
        "title": "List"
        })

        return context
