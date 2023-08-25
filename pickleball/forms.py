# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'active_player', 'is_staff', 'first_name', 'last_name', 'email', 'phone_number', 'level', 'league_type', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('level', 'active_player', 'is_staff', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'level', 'league_type')






