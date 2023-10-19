from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .form import *
import os
from django.conf import settings


API_URL = 'http://localhost:5000/'

# Create your views here.

def getAllprediction(self):
    # Récupérer les données
    response = requests.get(API_URL + 'predictAll')
    data = response.json()
    return render(request,'home/index.html',data)

def getOnePrediction(self, id):
    
      # Récupérer les données
    response = requests.get(API_URL + 'predict/' + str(id))
    data = response.json()
    return render(request,'home/index.html',data)


def predire(request):
    request_data = request.get_json()
    response = requests.post(API_URL + 'predictStudent/', json=request_data)
    data = response.json()
    return render(request,'home/index.html',data)
