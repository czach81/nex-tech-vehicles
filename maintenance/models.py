from django.db import models




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
