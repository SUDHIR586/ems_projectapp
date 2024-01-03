from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from accounts import models


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')
        model = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfileInfo
        fields = ('user_manager', 'user_work_hours', 'user_state', 'phone','email', 'adhar', 'street',
                  'house_number', 'city', 'post_code', 'image')
        labels = {
            'user_manager': 'Manager',
            'user_work_hours': 'Work hours',
            'user_state': 'Employee status',
            'phone': 'Phone',
            'email': 'email',
            'adhar': 'Aadhar',
            'street': 'Street',
            'house_number': 'House number',
            'city': 'City',
            'post_code': 'Zip code',
            'image': 'Photo'
        }

    def __init__(self, **kwargs):
        super(ProfileForm, self).__init__(**kwargs)
        self.fields['user_manager'].queryset = models.MyUser.objects.filter(is_superuser=True)



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.UserProfileInfo
        fields = ('phone', 'adhar', 'street',
                  'house_number', 'city', 'post_code', 'image')
        labels = {
            'phone': 'Telephone',
            'adhar': 'Aadhar',
            'street': 'Street',
            'house_number': 'House number',
            'city': 'City',
            'post_code': 'Zip code',
            'image': 'Photo'
        }
