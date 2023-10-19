from django import forms
from django.forms import fields
from utilisateur.models import *
from django.contrib.auth.models import User
    
    
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields ='__all__'

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'




class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['nom', 'niveau']

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['nom', 'prenom', 'classe', 'application_mode', 'displaced', 'debtor', 'tuition_fees_up_to_date', 'gender', 'scholarship_holder', 'age_at_enrollment', 'curricular_units_1st_sem_enrolled', 'curricular_units_1st_sem_approved', 'curricular_units_1st_sem_grade', 'curricular_units_2nd_sem_enrolled', 'curricular_units_2nd_sem_approved', 'curricular_units_2nd_sem_grade']



    
