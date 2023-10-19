# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Eleve
from .form import EleveForm

def eleve_list(request):
    eleves = Eleve.objects.all()
    return render(request, 'home/listedeseleves.html', {'eleves': eleves})

def eleve_detail(request, eleve_id):
    eleve = get_object_or_404(Eleve, pk=eleve_id)
    return render(request, 'eleve_detail.html', {'eleve': eleve})

def eleve_create(request):
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eleve_list')
    else:
        form = EleveForm()
    return render(request, 'eleve_form.html', {'form': form})

def eleve_update(request, eleve_id):
    eleve = get_object_or_404(Eleve, pk=eleve_id)
    if request.method == 'POST':
        form = EleveForm(request.POST, instance=eleve)
        if form.is_valid():
            form.save()
            return redirect('eleve_list')
    else:
        form = EleveForm(instance=eleve)
    return render(request, 'eleve_form.html', {'form': form})

def eleve_delete(request, eleve_id):
    eleve = get_object_or_404(Eleve, pk=eleve_id)
    eleve.delete()
    return redirect('eleve_list')
