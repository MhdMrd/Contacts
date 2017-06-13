from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.encoding import force_str
from django.core.signing import Signer
from django.contrib.auth.views import *
import os
from .forms import *
from .models import *
from django.contrib.auth import *
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

def acceuil(request):
    return HttpResponse("Bienvenue...")


def vide(request):
    return HttpResponse("C'est vide...")


def addContact(request):
    utilisateur = request.user
    profil_u = get_object_or_404(profil, user=utilisateur)
    contact = ContactAddForm(request.POST, request.FILES)
    if request.method == "POST":
        if contact.is_valid():
            new_contact = contact.save(commit=False)
            new_contact.user = auth.get_user(request)
            new_contact.save()
            return redirect('/contacts/list/')
    else:
        contact = ContactAddForm()
    return render(request, 'add_contact.html', {'form': contact, 'profil_u': profil_u})


def editContact(request, pk):
    utilisateur = request.user
    profil_u = get_object_or_404(profil, user=utilisateur)
    contact_to_edit = get_object_or_404(contact, pk=pk)
    form = ContactAddForm(request.POST, instance=contact_to_edit)
    if request.method == "POST":
        if form.is_valid():
            edited_contact = form.save()
            edited_contact.save()
            return redirect('/contacts/list/')
    else:
        form = ContactAddForm(instance=contact_to_edit)
    return render(request, 'edit_contact.html', {'form': form, 'profil_u': profil_u})

def detailsContact(request, pk) :
    contact_searched = get_object_or_404(contact, pk = pk)
    utilisateur = request.user
    profil_u = get_object_or_404(profil, user = utilisateur)
    url = contact_searched.photo.url
    pp = url.__getslice__(6, len(url))
    pps = str(pp)
    pp2 = pps.split('/')
    pp22 = pp2[3]
    return render(request, 'details_contact.html', {'profil_u':profil_u, 'contact':contact_searched, 'ppf':pp22})

@login_required(login_url='/accounts/login/')
def listContacts(request):
    utilisateur = request.user
    contacts = contact.objects.filter(user = utilisateur)
    profil_u = get_object_or_404(profil, user=utilisateur)
    url = profil_u.profile_photo.url
    pp = url.__getslice__(6, len(url))
    pps = str(pp)
    pp2 = pps.split('/')
    pp22 = pp2[3]
    return render(request, 'list_contacts.html', {'contacts':contacts, 'profil_u':profil_u, 'ppf':pp22})

def deleteContact(request, pk) :
    contact_to_delete = contact.objects.get(pk = pk).delete()
    return redirect('/contacts/list/')

def addUser(request):
    form = AddUserForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_user = User.objects.create_user(username=request.POST['pseudo'], email=request.POST['email'],password=request.POST['password'])
            new_profile.user = new_user
            new_profile.save()
            login(request, new_user)
            return redirect('/contacts/list')
    else:
        form = AddUserForm()
    return render(request, 'add_user.html', {'form': form})


def logout_user(request):
    auth.logout(request)
    session = request.session
    session.clear()
    return
def login_user(request):
    logout_user(request)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['username']= request.POST['username']
                    return redirect('/contacts/list/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})