# Generated by Django 4.0.3 on 2022-12-10 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_salcompanydetails_provident_fund_deduction_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salcompanydetails',
            old_name='provident_fund_deduction',
            new_name='Provident_Fund_deduction',
        ),
        migrations.RenameField(
            model_name='salcompanydetails',
            old_name='tds_deduction',
            new_name='TDS_deduction',
        ),
    ]
