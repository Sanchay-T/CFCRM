# Generated by Django 4.0.3 on 2022-12-16 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_proptype1_car_parking_amt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salincomedetails',
            name='deduction',
        ),
        migrations.RemoveField(
            model_name='salincomedetails',
            name='deduction_choice',
        ),
    ]
