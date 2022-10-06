
# Generated by Django 4.0.3 on 2022-10-01 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgreementType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement_type', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_type', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AreaIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('area_in', models.CharField(max_length=50)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AreaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('area_type', models.CharField(max_length=50)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AYYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('ay_year', models.CharField(max_length=7)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BankName',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BonusType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus_type', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),


        migrations.CreateModel(
            name='CibilLoanType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('cibil_loan_type', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),





        migrations.CreateModel(
            name='CibilType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('cibil_type', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('company_type', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_type', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeductionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('deduction_type', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('default_year', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DesignationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('desg_type', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_type', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IncentivesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('incentives_type', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_type', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LawyerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('lawyer_type', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeadSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_source', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LesseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('lesse_type', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoanAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.CharField(max_length=30)),
                ('min_loan_amount', models.IntegerField()),
                ('max_loan_amount', models.IntegerField()),
                ('total_exp', models.IntegerField()),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('marital_status', models.CharField(max_length=10)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),



        migrations.CreateModel(
            name='ProductsOrServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('products_or_services', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),

        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NatureOfBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nature_business', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NegativeArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('negative_area', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDelayYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_delay_year', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=5)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),

        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('property_in', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=25)),
                ('degree', models.BooleanField(default=False)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RateOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_of_interest', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RejectionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('rejection_type', models.CharField(max_length=45)),
                ('rejection_reason', models.CharField(max_length=60)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResidenceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('residence_type', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalaryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_type', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StageOfConstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=55)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_product', models.CharField(max_length=50)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='master.product')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(default='', max_length=25)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
                ('state', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='master.state')),
            ],
        ),
    ]
