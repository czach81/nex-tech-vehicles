from django.db import models
from django.conf import settings


leavingFrom_choices = (
    ('Agra-Central Office', 'Agra-Central Office'), 
    ('Almena - Central Office', 'Almena - Central Office'),
    ('Alton-Central Office', 'Alton-Central Office'), 
    ('Athol - Central Office', 'Althol - Central Office')
)

headingTo_choices = (
    ('Agra-Central Office', 'Agra-Central Office'), 
    ('Almena - Central Office', 'Almena - Central Office'),
    ('Alton-Central Office', 'Alton-Central Office'), 
    ('Athol - Central Office', 'Althol - Central Office')
)

recurrence_options = (
    ('Occurs one time', 'Occurs one time'), 
    ('Every Week', 'Every Week'),
    ('Every Month', 'Every Month') 
    
)

driver_choices = (
    ('dri 1', 'Dri 1'), 
    ('dri 2', 'Dri 2'), 
    ('dri 3', 'Dri 3')
)
passenger_choices = (
    ('pass 1', 'Pass 1'), 
    ('pass 2', 'Pass 2'), 
    ('pass 3', 'Pass 3')
)



class Reservation(models.Model):
    vehicle = models.ForeignKey('vehicle.Vehicle', on_delete=models.CASCADE, related_name='reservations')
    leaving_From = models.CharField(choices=leavingFrom_choices, max_length=40, blank=False, default=None)
    heading_To = models.CharField(choices=headingTo_choices, max_length=40, blank=False, default=None)
    leaving_By = models.DateTimeField(max_length=40)
    returning_By = models.DateTimeField(max_length=40)
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations_driver')
    passenger = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    purpose = models.TextField()
    additional_Comments = models.TextField( null=True, blank=True)
    
    def __str__(self):
        return str(self.vehicle)



    
   
    
   