# Generated by Django 4.0.3 on 2022-12-13 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
        ('account', '0015_alter_salcompanydetails_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salcompanydetails',
            name='company_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.companyname'),
        ),
    ]