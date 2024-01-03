from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext as _

# Create your models here.
class MyUser(AbstractUser):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('email').blank = False
        self._meta.get_field('email')._unique = True
        super(MyUser, self).__init__(*args, **kwargs)

    class Meta:
       app_label = 'accounts'

    def __str__(self):
        return "ID: " + str(self.id) +  " " + self.get_full_name()

class UserStateModel(models.Model):
    state_description = models.CharField(max_length=50, verbose_name='User status')

    def __str__(self):
            return self.state_description

class WorkHoursModel(models.Model):
    work_hour = models.CharField(max_length=4,null=True,blank=True)
    description = models.CharField(max_length=200, verbose_name='Description of the change')
    rate_of_pay = models.DecimalField(verbose_name='Pay rate', default=0, max_digits=3, decimal_places=2)

    def __str__(self):
            return self.description

class UserProfileInfo(models.Model):
    Attendance = (
        ('Present','Present'),
        ('Absent','Absent'),

    )

    WorkHours = (
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),
        ('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),
    )
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, verbose_name='User', related_name='user_profile')
    user_manager = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Manager', related_name='user_manager')
    user_work_hours = models.ForeignKey(WorkHoursModel,choices=WorkHours,null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name='Work hours', related_name='user_work_hours')
    user_state = models.ForeignKey(UserStateModel,choices=Attendance, null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name='User status', related_name='user_state')
    adhar = models.CharField(max_length=11, verbose_name='Aadhar')
    street = models.CharField(max_length=200, verbose_name='Street')
    city = models.CharField(max_length=200, verbose_name='City')
    phone = models.CharField(max_length=20, verbose_name='Phone Number')
    email = models.EmailField(blank=True,null=True)
    post_code = models.CharField(max_length=6, verbose_name='Zip code')
    house_number = models.CharField(max_length=20, verbose_name='House number')
    image = models.ImageField(upload_to='avatars/', default=None, null=True, blank=True)

    def __str__(self):
        return str(self.user.id) +', ' + self.user.get_full_name() + ',  Aadhar: ' + self.adhar

class UserAccessModel(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, verbose_name='User', related_name='user_access')
    rfid = models.CharField(max_length=200, verbose_name='rfid')
    comments = models.CharField(max_length=500, verbose_name='comments', null=True, blank=True)

    def __str__(self):
            return self.user.get_full_name() + ',  Aadhar: ' + self.adhar
