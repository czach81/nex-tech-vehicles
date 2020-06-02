from django.views.generic import FormView, UpdateView, CreateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import VehicleForm, VehicleStatusForm
from vehicle.models import Vehicle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

def contact(request):

    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():

            vehicle_Number = form.cleaned_data['vehicle_number']
            description = form.cleaned_data['description']
            employee = form.cleaned_data['employee']
            vehicle_Type = form.cleaned_data['vehicle_type']
            location  = form.cleaned_data['location']
            make = form.cleaned_data['make']
            model  = form.cleaned_data['model']
            year  = form.cleaned_data['year']
            mileage = form.cleaned_data['mileage']
            disposal_Date = form.cleaned_data['disposal_date']
            purchase_Date = form.cleaned_data['purchase_date']
            capacity = form.cleaned_data['capacity']
            tag_Number = form.cleaned_data['tag_Number']
            VIN = form.cleaned_data['VIN']
            cell_Phone = form.cleaned_data['cell_Phone']
            voice_Mail = form.cleaned_data['voice_Mail']
            gas_Card = form.cleaned_data['gas_Card']
            days_Driven = form.cleaned_data['days_Driven']
            fuel_Type= form.cleaned_data['fuel_Type']
            diposal_Mileage = form.cleaned_data['diposal_Mileage']
            comments = form.cleaned_data['comments']
            recieves_Messages = form.cleaned_data['recieves_Messages']
            active = form.cleaned_data['active']
            reminder_Type = form.cleaned_data['reminder_Type']

            print(vehicle_Number, description, employee, vehicle_Type, location, make, model, year,
            mileage, disposal_Date, purchase_Date, capacity, tag_Number, VIN, cell_Phone, voice_Mail, 
            gas_Card, days_Driven, fuel_Type, diposal_Mileage, comments, recieves_Messages, active, reminder_Type  )

    form = VehicleForm()
    return render(request, 'form.html', {'form': form})

class AddVehicleView(CreateView):
    form_class = VehicleForm
    template_name = "add_vehicle.html"

    def get_success_url(self):
        from django.urls import reverse
        return reverse('vehicle_list') 


    


class VehicleListView(FormView):
    form_class = VehicleStatusForm  #new form goes here for status 
    template_name = "list_vehicles.html"

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
        queryset = Vehicle.objects.all() # start here to be able to read get request query parameters for django 
        status = self.request.GET.get('status')
        if status == 'ACTIVE':
            queryset = queryset.filter(active = True)
        elif status == 'NONACTIVE':
            queryset = queryset.filter(active = False)

        queryset=queryset.order_by('vehicle_Number')

        paginator = Paginator(queryset, 5)

        page = self.request.GET.get('page')
        try:
          queryset = paginator.page(page)
        except PageNotAnInteger:
          queryset = paginator.page(1)
        except EmptyPage:
          queryset = paginator.page(paginator.num_pages)

        context.update({
        "object_list": queryset,
        "title": "List"
        })

        return context

class EditVehicleView(UpdateView):
    form_class = VehicleForm
    template_name = "edit_vehicle.html"

    model = Vehicle

    def get_success_url(self):
        from django.urls import reverse
        return reverse('vehicle_list') 





        


   

    
