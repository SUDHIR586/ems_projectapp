from django.db import models
from accounts.models import MyUser

# Create your models here.
class HolidayModel(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Employee', related_name='holiday_user')
    approver_user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING,  null=True, blank=True, default=None, verbose_name='Approver', related_name='holiday_approver_user')
    start_date = models.DateField(verbose_name='Start date')
    end_date = models.DateField(verbose_name='end date')
    is_used = models.BooleanField(default=False, verbose_name='Is completed')
    is_approved = models.BooleanField(default=False, verbose_name='Whether approved')

    def __str__(self):
        return "Free: " + self.user.get_full_name() + " Aadhar: " + self.user.user_profile.adhar_number + "  From: " + str(self.start_date) + " To: " + str(self.end_date)
