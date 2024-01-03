# Generated by Django 4.2.7 on 2023-12-31 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_app', '0001_initial'),
        ('resources_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntranceExitReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_description', models.CharField(max_length=200, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='EntranceExitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Whether approved')),
                ('place', models.CharField(max_length=200, verbose_name='Place')),
                ('fromExitToEntranceTimestamp', models.IntegerField(blank=True, default=None, null=True, verbose_name='Time')),
                ('approver_user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='entrance_exit_approver_user', to=settings.AUTH_USER_MODEL, verbose_name='Approver')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrance_exit_project', to='project_app.projectmodel', verbose_name='Project')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entrance_exit_reason', to='ems_app.entranceexitreason', verbose_name='Reason')),
                ('resource', models.ManyToManyField(blank=True, default=None, related_name='entrance_exit_resource', to='resources_app.resourcemodel', verbose_name='Resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entrance_exit_user', to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
            ],
        ),
    ]
