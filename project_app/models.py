from django.db import models
from accounts.models import MyUser

# Create your models here.

class ProjectModel(models.Model):
    id_employee = models.ManyToManyField(MyUser,  verbose_name='Employee', related_name='project_employee_user')
    id_project_pm = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Project Manager', related_name='project_pm_user', null=True, blank=True)
    client = models.CharField(max_length=300, verbose_name='Customer name')
    name = models.CharField(max_length=200, verbose_name='Name')
    number1 = models.IntegerField(verbose_name='Project number1')
    number2 = models.IntegerField(verbose_name='Project number2')
    project_type = models.CharField(max_length=50, verbose_name='Project type')
    status = models.CharField(max_length=50, verbose_name='Status')
    start_date = models.DateField(verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')
    contact = models.CharField(max_length=500, verbose_name='Contact')
    commants = models.TextField(max_length=500, verbose_name='Comments', null=True, blank=True)

    def __str__(self):
        return self.name+" number1: "+ str(self.number1) +" number2: " + str(self.number2) + " project_pm: " + self.id_project_pm.get_full_name()
