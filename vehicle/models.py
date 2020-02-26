from django.db import models

class Vehicle(models.Model):
    vehicle_Number = models.IntegerField()
    description = models.CharField(max_length=40)
    employee = models.CharField(choices=[('emp 1', 'Emp 1'), ('emp 2', 'Emp 2')], max_length=255)
    vehicle_Type = models.CharField(choices=[('veh 1', 'Veh 1'), ('veh 2', 'Veh 2')], max_length=255)
    location = models.CharField(choices=[('loc 1', 'Loc 1'), ('loc 2', 'Loc 2')], max_length=255)
    make = models.CharField(max_length=40) #read only
    model = models.CharField(max_length=40) #read only
    year = models.CharField(max_length=40)  #read only
    purchase_Date = models.DateField(max_length=40)
    disposal_Date = models.DateField(max_length=40)
    mileage = models.IntegerField()
    capacity = models.CharField(max_length=40) #
    tag_Number = models.CharField(max_length=40)
    VIN = models.CharField(max_length=40)
    cell_Phone = models.IntegerField()
    voice_Mail = models.CharField(max_length=40)
    gas_Card = models.CharField(max_length=40)
    days_Driven = models.BooleanField() #checkbox/radio button ///required field
    fuel_Type = models.CharField(choices=[('gasoline', 'Gasoline'), ('diesel', 'Diesel')], max_length=40)
    diposal_Mileage = models.IntegerField()
    comments = models.CharField(max_length=255)
    recieves_Messages = models.BooleanField() # radio button
    active = models.BooleanField() # radio button
    reminder_Type = models.CharField(choices=
    [('none', 'None'), ('oil change', 'Oil Change'), ('tire rotation', 'Tire Rotation'),('both', 'Both')], max_length=40)

    def __str__(self):
        return str(self.vehicle_Number)
        
