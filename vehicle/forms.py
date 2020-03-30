from django import forms
from .models import Vehicle, STATUS_CHOICES



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

    
