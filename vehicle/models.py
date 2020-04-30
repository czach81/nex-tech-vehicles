from django.db import models


STATUS_CHOICES = [
    ('ACTIVE', 'Active'),
    ('NONACTIVE', 'Non-Active'),
    ('ALL', 'ALL')
]

class Vehicle(models.Model):
    vehicle_Number = models.IntegerField()
    description = models.CharField(max_length=40)
    employee = models.CharField(choices=[('emp 1', 'Emp 1'), ('emp 2', 'Emp 2'), ('emp 3', 'Emp 3')], max_length=255)
    vehicle_Type = models.CharField(choices=[('veh 1', 'Veh 1'), ('veh 2', 'Veh 2'), ('veh 3', 'Veh 3')], max_length=255)
    location = models.CharField(choices=[('loc 1', 'Loc 1'), ('loc 2', 'Loc 2'), ('loc 3', 'Loc 3')], max_length=255)
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
    disposal_Mileage = models.IntegerField()
    comments = models.CharField(max_length=255)
    recieves_Messages = models.BooleanField() # radio button
    active = models.BooleanField() # radio button
    reminder_Type = models.CharField(choices=
    [('none', 'None'), ('oil change', 'Oil Change'), ('tire rotation', 'Tire Rotation'),('both', 'Both')], max_length=40)
    
    def __str__(self):
        return str(self.vehicle_Number)


class Maintenance(models.Model):
    vehicle = models.ForeignKey('vehicle.Vehicle', on_delete=models.CASCADE, related_name='maintenance')
    mileage = models.IntegerField()
    maintenance_Date = models.IntegerField(max_length=40)
    changed_Oil = models.BooleanField()
    rotated_Tires = models.BooleanField()
    changed_Transmission_Fluid = models.BooleanField()
    comments = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.vehicle)

class Mileage(models.Model):
    
    month_End_Mileage = models.IntegerField(max_length=40)
    first_Aid_Kit_Status = models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], max_length=40, blank=False, default=None)
    fire_Extinguisher_Status = models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], max_length=40, blank=False, default=None)
    drugalcohol_Testing_Kit_Status = models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], max_length=40, blank=False, default=None)
    vehicle = models.ForeignKey('vehicle.Vehicle', on_delete=models.CASCADE, related_name='mileage_entry')
    no_Days_Commuted = models.BooleanField()
    year = models.IntegerField(choices=[( 2020, '2020'), ( 2021, '2021'), ( 2022, '2022'),
    ( 2023, '2023'), ( 2024, '2024'), ( 2025, '2025'),
    ( 2026, '2026')], max_length=255)
    month = models.IntegerField(choices=[( 1, '1'), ( 2, '2'), ( 3, '3'),
    ( 4, '4'), ( 5, '5'), ( 6, '6'),
    ( 7, '7'), ( 8, '8'), ( 9, '9'),
    ( 10, '10'), ( 11, '1'), ( 12, '12')], max_length=255)
    day01 = models.BooleanField()
    day02 = models.BooleanField()
    day03 = models.BooleanField()
    day04 = models.BooleanField()
    day05 = models.BooleanField()
    day06 = models.BooleanField()
    day07 = models.BooleanField()
    day08 = models.BooleanField()
    day09 = models.BooleanField()
    day10 = models.BooleanField()
    day11 = models.BooleanField()
    day12 = models.BooleanField()
    day13 = models.BooleanField()
    day14 = models.BooleanField()
    day15 = models.BooleanField()
    day16 = models.BooleanField()
    day17 = models.BooleanField()
    day18 = models.BooleanField()
    day19 = models.BooleanField()
    day20 = models.BooleanField()
    day21 = models.BooleanField()
    day22 = models.BooleanField()
    day23 = models.BooleanField()
    day24 = models.BooleanField()
    day25 = models.BooleanField()
    day25 = models.BooleanField()
    day26 = models.BooleanField()
    day27 = models.BooleanField()
    day28 = models.BooleanField()
    day29 = models.BooleanField()
    day30 = models.BooleanField()
    day31 = models.BooleanField()



    def __str__(self):
        return str(self.vehicle)



        
