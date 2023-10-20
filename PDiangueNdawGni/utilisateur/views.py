from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count
from .models import *
import requests
from .form import *

from django.shortcuts import render
from django.http import JsonResponse
import os
from django.conf import settings
# Create your views here.
def index(request):
    classes = Classe.objects.annotate(nombre_eleves=Count('eleve')).order_by('-pk')
    return render(request,'home/index.html',{'classes':classes})


def liste_classes(request):
    classes = Classe.objects.annotate(nombre_eleves=Count('eleve'))
    return render(request, 'home/listedesclasses.html', {'classes': classes})

def liste_eleves_par_classe(request, classe_id):
    classe = Classe.objects.get(pk=classe_id)
    eleves = Eleve.objects.filter(classe=classe).order_by('-pk')
    
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
    eleves = Eleve.objects.all().order_by('-pk')
    return render(request,'home/predictions.html',{'eleves':eleves
    })

def listeFormation(request):
    return render(request,'home/liste_formation.html')

def listeEleves(request):
    return render(request,'home/listedeseleves.html')


# views.py



def update_eleve_fields(request, eleve_id):
    eleve = Eleve.objects.get(pk=eleve_id)
    
    classe = Classe.objects.get(pk=eleve.classe.id)
    # Appelez l'API de prédiction
    prediction_api_url = 'http://localhost:5000/predictStudent/'
    eleve_displaced = True if eleve.displaced else False
    eleve_debtor = True if eleve.debtor else False
    eleve_tuition_fees_up_to_date = True if eleve.tuition_fees_up_to_date else False
    eleve_scholarship_holder = True if eleve.scholarship_holder else False

    # Convertir le champ gender
    eleve_gender = 1 if eleve.gender == 'Female' else 0
    eleves_json = []
    # Créer un dictionnaire pour chaque élève avec tous les champs
    eleve_data = {
        
        'nom': eleve.nom,
        'prenom': eleve.prenom,
        'application_mode': eleve.application_mode,
        'displaced': eleve_displaced,
        'debtor': eleve_debtor,
        'tuition_fees_up_to_date': eleve_tuition_fees_up_to_date,
        'gender': eleve_gender,
        'scholarship_holder': eleve_scholarship_holder,
        'age_at_enrollment': eleve.age_at_enrollment,
        'curricular_units_1st_sem_enrolled': eleve.curricular_units_1st_sem_enrolled,
        'curricular_units_1st_sem_approved': eleve.curricular_units_1st_sem_approved,
        'curricular_units_1st_sem_grade': eleve.curricular_units_1st_sem_grade,
        'curricular_units_2nd_sem_enrolled': eleve.curricular_units_2nd_sem_enrolled,
        'curricular_units_2nd_sem_approved': eleve.curricular_units_2nd_sem_approved,
        'curricular_units_2nd_sem_grade': eleve.curricular_units_2nd_sem_grade,
        
    }

    eleves_json.append(eleve_data)

    
    # response = requests.post(prediction_api_url, eleves_json)
    response= requests.post(prediction_api_url, json=eleve_data)
    
    if response.status_code == 200:
        prediction_result = response.json()
        print(prediction_result)
        # Mettez à jour les champs en fonction du résultat de la prédiction
        eleve.risque_abandon = prediction_result['proba_dropout']
        eleve.proba_reussite = 100-prediction_result['proba_dropout']
        
        # Enregistrez les modifications dans la base de données
        try:
            eleve.save()
            print("Eleve enregistré avec succès")
        except Exception as e:
            # Gérer l'erreur, par exemple en affichant un message d'erreur
            print(f"Erreur lors de l'enregistrement de l'élève : {e}")

        classe = Classe.objects.get(pk=eleve.classe.id)
        eleves = Eleve.objects.filter(classe=classe).order_by('-pk')
        
        return render(request, 'home/listedeseleves.html', {'eleves': eleves, 'classe': classe})
    else:
        return JsonResponse({'status': 'error', 'message': 'Failed to get prediction result'})

