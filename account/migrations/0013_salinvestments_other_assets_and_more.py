# Generated by Django 4.0.3 on 2022-12-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_salinvestments_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='salinvestments',
            name='Other_Assets',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='salinvestments',
            name='Other_Owned_Property_Details',
            field=models.CharField(default=None, max_length=100),
        ),
    ]