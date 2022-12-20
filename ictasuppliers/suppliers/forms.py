from django import forms
from .models import Supplier
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UsernameField  

User = get_user_model()

class SupplierModelForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = (
            'name',
        )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =("username",)
        field_classes ={'username': UsernameField }