# Generated by Django 4.0.3 on 2022-12-16 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_salincomedetails_other_bank_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salincomedetails',
            name='net_sal',
            field=models.PositiveIntegerField(),
        ),
    ]
