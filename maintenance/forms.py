from django import forms
from .models import Maintenance, Mileage 





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



class MaintenanceForm(forms.ModelForm):

    class Meta:
        model = Maintenance
        exclude = ()
        widgets = {
            'vehicle': forms.HiddenInput(),
            'mileage': forms.NumberInput(attrs={'class': 'form-control'}),
            'maintenance_Date': forms.DateInput(attrs={'class': 'form-control'}),
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
            'vehicle': forms.HiddenInput(),

        }