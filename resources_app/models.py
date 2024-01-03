from django.db import models
from accounts.models import MyUser

# Create your models here.
class ResourceStateModel(models.Model):
    state_description = models.CharField(max_length=50, verbose_name='Resource status')

    def __str__(self):
        return self.state_description

class ResourceModel(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, null=True, blank=True, default=None, verbose_name='Employee', related_name='resource_user')
    approver_user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING,  null=True, blank=True, default=None, verbose_name='Approver', related_name='resource_approver_user')
    is_approved = models.BooleanField(default=False, verbose_name='Whether approved')
    is_available = models.BooleanField(default=True, verbose_name='Is available')
    name = models.CharField(max_length=200, default=None, verbose_name='Resource name')
    start_date = models.DateField(default=None, null=True, blank=True, verbose_name='Date of assignment')
    end_date = models.DateField(default=None, null=True, blank=True, verbose_name='end date')
    production_year = models.DateField(verbose_name='date of production')
    resource_state = models.ForeignKey(ResourceStateModel, on_delete=models.DO_NOTHING, verbose_name='Resource status', related_name='resource_state')
    image = models.ImageField(upload_to='resources/', default=None, null=True, blank=True, verbose_name="Photo")
    brand = models.CharField(max_length=200, default=None, verbose_name='Resource brand')
    model = models.CharField(max_length=200, default=None, verbose_name='Resource model')
    info =  models.TextField(max_length=500, verbose_name='Comments', null=True, blank=True)

    def __str__(self):
        return self.name + " state: " + str(self.resource_state) + " whether_available: "  + str(self.is_available)

class ResourceHistoryModel(models.Model):
    resource = models.ForeignKey(ResourceModel, on_delete=models.DO_NOTHING, verbose_name='Resource')
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Employee', related_name='resource_history_user')
    start_date = models.DateField(default=None, null=True, blank=True, verbose_name='Date of assignment')
    end_date = models.DateField(default=None, null=True, blank=True, verbose_name='end date')
    approver_user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Approver', related_name='resource_history_approver_user')
    start_date = models.DateField(verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')

    def __str__(self):
        return str(self.resource)


class FuelType(models.Model):
    fuel_type_description = models.CharField(max_length=100, verbose_name='Fuel type')

    def __str__(self):
        return self.fuel_type_description

class AutoModel(models.Model):
    resource = models.OneToOneField(ResourceModel, on_delete=models.DO_NOTHING, verbose_name='Employee', related_name='resource_auto')
    fuel_type = models.ForeignKey(FuelType, null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name='Fuel Type', related_name='auto_fuel_type')
    fuel_card_number = models.IntegerField(verbose_name='Fuel card number')
    registration_number = models.CharField(max_length=30, verbose_name='Registration number')
    car_meter_status = models.DecimalField(verbose_name='Meter status', max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.resource)
