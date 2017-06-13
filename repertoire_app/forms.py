from __future__ import unicode_literals
from django.contrib.auth.models import *
from django.forms import *
from .models import *
from django.forms import ModelForm
class ContactAddForm(ModelForm):
    class Meta :
        model = contact
        fields = ( 'pseudo','nom', 'prenom', 'numero','email','photo',)


class AddUserForm(ModelForm) :
    class Meta :
        model = profil
        fields =('pseudo','nom','prenom','numero','email', 'password','statut', 'profile_photo',)

class LoginForm(forms.Form) :
    username = CharField(max_length=255)
    password = PasswordInput()