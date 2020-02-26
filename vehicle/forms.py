from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Vehicle

"""class VehicleForm(forms.Form):
    vehicle_number = forms.IntegerField()
    description = forms.CharField()
    vehicle_Type = forms.ChoiceField(choices=[('veh 1', 'Veh 1'), ('veh 2', 'Veh 2')])
    location = forms.ChoiceField(choices=[('spot 1', 'Spot 1'), ('spot 2', 'Spot 2')])
    purchase_date = forms.DateField()
    disposal_date = forms.DateField()
    mileage = forms.IntegerField()
    employee = forms.ChoiceField(choices=[('emp 1', 'Emp 1'), ('emp 2', 'Emp 2')])
    make = forms.CharField() #read only
    model = forms.CharField() #read only
    year = forms.CharField()  #read only
    capacity = forms.CharField() 
    tag_number = forms.CharField()
    VIN = forms.CharField()
    cell_phone = forms.IntegerField()
    voice_mail = forms.CharField()
    gas_card = forms.CharField()
    days_driven = forms.BooleanField() #checkbox/radio button ///required field
    fuel_type = forms.ChoiceField(choices=[('gasoline', 'Gasoline'), ('diesel', 'Diesel')])
    diposal_mileage = forms.IntegerField()
    comments = forms.CharField()
    recieves_messages = forms.BooleanField() # radio button
    active = forms.BooleanField() # radio button
    reminder_type = forms.ChoiceField(choices=
    [('none', 'None'), ('oil change', 'Oil Change'), ('tire rotation', 'Tire Rotation'),('both', 'Both')])"""


    

class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'vehicle_Number',
            'description',
            'vehicle_Type',
            'location',
            'purchase_Date',
            'disposal_Date',
            'mileage',
            'make',
            'model',
            'year',
            'capacity',
            'tag_Number',
            'VIN',
            'cell_Phone',
            'voice_Mail',
            'gas_Card',
            'employee',
            'days_Driven',
            'fuel_Type',
            'diposal_Mileage',
            'comments',
            'recieves_Messages',
            'active',
            'reminder_Type',
            Submit('submit', 'Save', css_class='btn-success')
        )
