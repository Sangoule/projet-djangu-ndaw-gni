from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count
from .models import User
from .form import *
import os
from django.conf import settings
# Create your views here.
def index(request):
    classes=Classe.objects.all()
    return render(request,'home/index.html',{'classes':classes})


def liste_classes(request):
    classes = Classe.objects.annotate(nombre_eleves=Count('eleve'))
    return render(request, 'home/listedesclasses.html', {'classes': classes})

def liste_eleves_par_classe(request, classe_id):
    classe = Classe.objects.get(pk=classe_id)
    eleves = Eleve.objects.filter(classe=classe)
    return render(request, 'home/listedeseleves.html', {'classe': classe, 'eleves': eleves})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('user-list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

def register_user_profil(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_list')
    else:
        user_form = RegistrationForm()
        profile_form = UserProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'gestion-utilisateur/create_user.html', context)

def user_list(request):
    users = User.objects.all()
    profiles = UserProfile.objects.all()

    context = {
        'users': users,
        'profiles': profiles
    }

    return render(request, 'gestion-utilisateur/liste-utilisateur.html', context)



def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        # Supprimer l'utilisateur de la base de données
        user.delete()

        return redirect('user_list')

    context = {
        'user': user
    }

    return render(request, 'delete_utilisateur/delete_user.html', context)

def edit_profile(request, idUser):
    profile = get_object_or_404(UserProfile, idUser=idUser)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'gestion-utilisateur/edit_user.html', context)

def donnes(request):
    return render(request,'home/donnes_solaires.html')

def predictions(request):
    return render(request,'home/predictions.html')

def listeFormation(request):
    return render(request,'home/liste_formation.html')

def listeEleves(request):
    return render(request,'home/listedeseleves.html')
