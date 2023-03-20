from cProfile import label
from dataclasses import fields
from email.headerregistry import Group
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group, Permission
from  django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm


class UserGroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields='__all__'
        

class CreateUser(UserCreationForm):
    email = forms.EmailField(
        label='Email',
    )
   
    user_permissions = forms.TextInput(
    )
    
   
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = '__all__'
        
        
        def user_perm(self):
            user_ps = Permission.objects.all()
            userp = []
            for u in user_ps:
                userp.append(u)
            
