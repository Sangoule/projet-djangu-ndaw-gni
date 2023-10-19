# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Classe, Eleve
from .form import ClasseForm, EleveForm

def classe_list(request):
    classes = Classe.objects.all()
    return render(request, 'classe_list.html', {'classes': classes})

def classe_detail(request, classe_id):
    classe = get_object_or_404(Classe, pk=classe_id)
    return render(request, 'classe_detail.html', {'classe': classe})

def classe_create(request):
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classe_list')
    else:
        form = ClasseForm()
    return render(request, 'classe_form.html', {'form': form})

def classe_update(request, classe_id):
    classe = get_object_or_404(Classe, pk=classe_id)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('classe_list')
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'classe_form.html', {'form': form})

def classe_delete(request, classe_id):
    classe = get_object_or_404(Classe, pk=classe_id)
    classe.delete()
    return redirect('classe_list')

# Les vues pour les élèves suivront une structure similaire...
