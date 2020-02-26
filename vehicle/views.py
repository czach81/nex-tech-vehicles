from django.shortcuts import render
from django.http import HttpResponse
from .forms import VehicleForm 

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

def Vehicle_models_detail(request):

    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()


    form = VehicleForm()
    return render(request, 'form.html', {'form': form})
