from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class contact(models.Model) :
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    pseudo = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    numero = models.IntegerField(null=False)
    photo = models.ImageField(null=True, blank=True, upload_to="static/images/Photos contacts/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,default=False)
    def __str__(self):
        return u""+self.pseudo +" - %s" %self.numero


class profil(models.Model) :
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=60, null=False)
    password = models.CharField(max_length=15, null=False, default=False)
    email = models.EmailField()
    numero = models.IntegerField(null=False)
    statut = models.CharField(max_length=150, default="Aucun statut")
    profile_photo = models.ImageField(null=True, blank=True, upload_to="static/images/Photos de profils/")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, default=False, unique=True )
    def __str__(self):
        return "%s"%self.pseudo