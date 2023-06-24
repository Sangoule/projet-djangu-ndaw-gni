from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from reserver.models import *
from reserver.form import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import os
from django.conf import settings

def index(request):
    return render(request,'index.html')
def profile(request):
    return render(request,'home/profile.html')
def about(request):
    return render(request,'about.html')
def vols(request):
    vols=Vol.objects.all()
    context={'vols':vols}
    return render(request,'vols/acceuils_vols.html',context)
def compagnies(request):
    compagnies=Compagnie.objects.all()
    context={'compagnies':compagnies}
    return render(request,'compagnies/accueil_cie.html',context)
def volsdetails(request,id):
    vols=Vol.objects.get(pk=id)
    context={'vols':vols}
    return render(request,'vols/vols.html',context)
def trajects(request):
    trajects=Trajet.objects.all()
    context={'trajects':trajects}
    return render(request,'trajets/accueil_traject.html',context)

def modif_comp(request,id):
    comp = Compagnie.objects.get(pk=id)
    form= CompagnieForm()
    context={'comp':comp,'form':form}
    return render(request, 'compagnies/comp_form.html', context)

def compagnie_update(request, id):
    comp = Compagnie.objects.get(pk=id)
    if request.method == 'POST':
        form = CompagnieForm(request.POST,request.FILES, instance=comp)
        if form.is_valid():
            form.save()
            return redirect('compagnies')
    else: 
        CompagnieForm(instance=comp)
    return render(request, 'compagnies/comp_form.html', {'form': form})

def del_vol(request,id):
    vol=Vol.objects.get(pk=id)
    vol.delete()
    return redirect('vols')
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


