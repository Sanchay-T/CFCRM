# Generated by Django 4.0.3 on 2022-12-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_salotherincomes_rental_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='salcompanydetails',
            name='other_company_name',
            field=models.TextField(default=None, max_length=20),
        ),
    ]
