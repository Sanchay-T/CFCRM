# Generated by Django 4.0.3 on 2022-12-13 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
        ('account', '0014_alter_salcompanydetails_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salcompanydetails',
            name='company_name',
            field=models.ForeignKey(blank=True, choices=[('other', 'other'), ('other', 'other')], default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.companyname'),
        ),
    ]
