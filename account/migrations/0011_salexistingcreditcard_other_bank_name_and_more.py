# Generated by Django 4.0.3 on 2022-12-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_rename_provident_fund_deduction_salcompanydetails_provident_fund_deduction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salexistingcreditcard',
            name='other_bank_name',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='salexistingloandetails',
            name='other_bank_name',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
