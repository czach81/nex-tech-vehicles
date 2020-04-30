from django import forms
from .models import Vehicle, STATUS_CHOICES, Maintenance, Mileage 



employee_choices = (
  ('emp 1', 'Emp 1'),
  ('emp 2', 'Emp 2'),
  ('emp 3', 'Emp 3'),
)

vehicle_choices = (
  ('veh 1', 'Veh 1'),
  ('veh 2', 'Veh 2'),
  ('veh 3', 'Veh 3'),
)

location_choices = (
  ('loc 1', 'Loc 1'),
  ('loc 2', 'Loc 2'),
  ('loc 3', 'Loc 3'),
)

fuel_choices= (
  ('gasoline', 'Gasoline'),
  ('diesel', 'Diesel'),  
)

reminder_choices = (
  ('none', 'None'),
  ('oil change', 'Oil Change'),
  ('tire rotation', 'Tire Rotation'),
  ('both', 'Both'),
)

year_choices = (
  ('2020', '2020'), 
  ('2021', '2021'), ('2022', '2022'),
  ('2023', '2023'), ('2024', '2024'), 
  ('2025', '2025'),
  ('2026', '2026')
)

month_choices = (
  ('january', 'January'), ('february', 'February'), ('march', 'March'),
  ('april', 'April'), ('may', 'May'), ('june', 'June'),
  ('july', 'July'), ('august', 'August'), ('september', 'September'),
  ('october', 'October'), ('november', 'November'), ('december', 'December')
)

goodorbad_choices = (
  ('good', 'Good'), 
  ('bad', 'Bad')
)

class VehicleStatusForm(forms.Form):
    status = forms.CharField(max_length=100, widget=forms.Select(choices= STATUS_CHOICES))


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        exclude = ()
        widgets = {
            'vehicle_Number': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}, choices=employee_choices),
            'vehicle_Type': forms.Select(attrs={'class': 'form-control'}, choices=vehicle_choices),
            'location': forms.Select(attrs={'class': 'form-control'}, choices=location_choices),
            'make': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'purchase_Date': forms.TextInput(attrs={'class': 'form-control'}),
            'disposal_Date': forms.TextInput(attrs={'class': 'form-control'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'tag_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'VIN': forms.TextInput(attrs={'class': 'form-control'}),
            'cell_Phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'voice_Mail': forms.TextInput(attrs={'class': 'form-control'}),
            'gas_Card': forms.NumberInput(attrs={'class': 'form-control'}),
            'days_Driven': forms.CheckboxInput(attrs={'class': 'form-control'}),    #radiobutton
            'fuel_Type': forms.Select(attrs={'class': 'form-control'}, choices=fuel_choices),
            'disposal_Mileage': forms.NumberInput(attrs={'class': 'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
            'recieves_Messages': forms.CheckboxInput(attrs={'class': 'form-control'}),  #radiobutton   
            'active': forms.CheckboxInput(attrs={'class': 'form-control'}),   #radiobutton
            'reminder_Type': forms.Select(attrs={'class': 'form-control'}, choices=reminder_choices),
            
        }

class MaintenanceForm(forms.ModelForm):

    class Meta:
        model = Maintenance
        exclude = ()
        widgets = {
            'mileage': forms.NumberInput(attrs={'class': 'form-control'}),
            'maintenance_Date': forms.NumberInput(attrs={'class': 'form-control'}),
            'changed_Oil': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'rotated_Tires': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'changed_Transmission_Fluid': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),

        }

class MileageForm(forms.ModelForm):

    class Meta:
        model = Mileage
        exclude = ()
        widgets = {
            'year': forms.Select(attrs={'class': 'form-control'}, choices=year_choices),
            'month': forms.Select(attrs={'class': 'form-control'}, choices=month_choices),
            'month_End_Mileage': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_Aid_Kit_Status': forms.RadioSelect(attrs={'class': 'my-radio'}),
            'fire_Extinguisher_Status': forms.RadioSelect(attrs={'class': 'my-radio'}),
            'drugalcohol_Testing_Kit_Status': forms.RadioSelect(attrs={'class': 'my-radio'}),

        }

    
