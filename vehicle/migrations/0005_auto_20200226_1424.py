# Generated by Django 3.0.3 on 2020-02-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_auto_20200226_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_number',
            new_name='cell_Phone',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='VIN',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='capacity',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='comments',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='days_Driven',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='diposal_Mileage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='disposal_Date',
            field=models.DateField(default='2020-02-26', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='employee',
            field=models.CharField(choices=[('emp 1', 'Emp 1'), ('emp 2', 'Emp 2')], default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuel_Type',
            field=models.CharField(choices=[('gasoline', 'Gasoline'), ('diesel', 'Diesel')], default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='gas_Card',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='location',
            field=models.CharField(choices=[('loc 1', 'Loc 1'), ('loc 2', 'Loc 2')], default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='make',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='mileage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='purchase_Date',
            field=models.DateField(default='2020-02-26', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='recieves_Messages',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='reminder_Type',
            field=models.CharField(choices=[('none', 'None'), ('oil change', 'Oil Change'), ('tire rotation', 'Tire Rotation'), ('both', 'Both')], default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='tag_Number',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_Number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_Type',
            field=models.CharField(choices=[('veh 1', 'Veh 1'), ('veh 2', 'Veh 2')], default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='voice_Mail',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='year',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]