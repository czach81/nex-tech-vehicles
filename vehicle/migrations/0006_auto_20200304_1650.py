# Generated by Django 3.0.3 on 2020-03-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_auto_20200226_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='diposal_Mileage',
            new_name='disposal_Mileage',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='employee',
            field=models.CharField(choices=[('emp 1', 'Emp 1'), ('emp 2', 'Emp 2'), ('emp 3', 'Emp 3')], max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='location',
            field=models.CharField(choices=[('loc 1', 'Loc 1'), ('loc 2', 'Loc 2'), ('loc 3', 'Loc 3')], max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_Type',
            field=models.CharField(choices=[('veh 1', 'Veh 1'), ('veh 2', 'Veh 2'), ('veh 3', 'Veh 3')], max_length=255),
        ),
    ]