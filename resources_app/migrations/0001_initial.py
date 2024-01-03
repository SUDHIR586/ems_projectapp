# Generated by Django 4.2.7 on 2023-12-31 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type_description', models.CharField(max_length=100, verbose_name='Fuel type')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceStateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_description', models.CharField(max_length=50, verbose_name='Resource status')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Whether approved')),
                ('is_available', models.BooleanField(default=True, verbose_name='Is available')),
                ('name', models.CharField(default=None, max_length=200, verbose_name='Resource name')),
                ('start_date', models.DateField(blank=True, default=None, null=True, verbose_name='Date of assignment')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='end date')),
                ('production_year', models.DateField(verbose_name='date of production')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='resources/', verbose_name='Photo')),
                ('brand', models.CharField(default=None, max_length=200, verbose_name='Resource brand')),
                ('model', models.CharField(default=None, max_length=200, verbose_name='Resource model')),
                ('info', models.TextField(blank=True, max_length=500, null=True, verbose_name='Comments')),
                ('approver_user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_approver_user', to=settings.AUTH_USER_MODEL, verbose_name='Approver')),
                ('resource_state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_state', to='resources_app.resourcestatemodel', verbose_name='Resource status')),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_user', to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('approver_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_history_approver_user', to=settings.AUTH_USER_MODEL, verbose_name='Approver')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='resources_app.resourcemodel', verbose_name='Resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_history_user', to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
            ],
        ),
        migrations.CreateModel(
            name='AutoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_card_number', models.IntegerField(verbose_name='Fuel card number')),
                ('registration_number', models.CharField(max_length=30, verbose_name='Registration number')),
                ('car_meter_status', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Meter status')),
                ('fuel_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='auto_fuel_type', to='resources_app.fueltype', verbose_name='Fuel Type')),
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_auto', to='resources_app.resourcemodel', verbose_name='Employee')),
            ],
        ),
    ]
