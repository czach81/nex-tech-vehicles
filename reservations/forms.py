from django import forms
from .models import Reservation, leavingFrom_choices, headingTo_choices
from django.contrib.auth import get_user_model

User=get_user_model()








class MakeReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('leaving_From', 'heading_To', 'leaving_By', 'returning_By')
        widgets = {
            'leaving_From': forms.Select(attrs={'class': 'form-control'}, choices=leavingFrom_choices),
            'heading_To': forms.Select(attrs={'class': 'form-control'}, choices=headingTo_choices),
            'leaving_By': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'returning_By': forms.DateTimeInput(attrs={'class': 'form-control'}),
            

        }
class SelectVehicleReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('vehicle',)
        widgets = {
            
            'vehicle': forms.HiddenInput()
        }


class DetailReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('driver', 'passenger', 'purpose', 'additional_Comments')
        widgets = {
            
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'passenger': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'additional_Comments': forms.TextInput(attrs={'class': 'form-control'}),
            

        }