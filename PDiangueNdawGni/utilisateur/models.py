from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from safedelete.managers import SafeDeleteManager
from safedelete.models import SafeDeleteModel
import uuid
from django_resized import ResizedImageField
from utilisateur.validators import *
from safedelete.config import DELETED_INVISIBLE

        # Votre code pour créer un super-utilisateur
ADMIN = 'admin'
DIRECTEUR = 'directeur'
SUPERADMIN = 'superadmin'
PENDING = 'pending'
OTHERS = 'others'
DELETED = 'deleted'

USER_TYPES = (
    (ADMIN, ADMIN),
    (DIRECTEUR, DIRECTEUR),
    (SUPERADMIN, SUPERADMIN),
    (PENDING, PENDING),
)
ADMIN_TYPE = (
    (ADMIN, ADMIN),
    (SUPERADMIN, SUPERADMIN)
)


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#     profil= models.CharField(max_length=50, unique=False)
#     avatar = models.ImageField(upload_to='media/', null=True, blank=True)

#     def __str__(self):
#         return self.user.username

class MyModelManager(SafeDeleteManager):
    _safedelete_visibility = DELETED_INVISIBLE


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('user_type', SUPERADMIN)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin, SafeDeleteModel):
    slug = models.UUIDField(default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=255,validators=[isnumbervalidator],unique=True)
    
    adresse = models.CharField(max_length=1000, null=True,blank=True)
    boite_postal = models.CharField(max_length=1000, null=True,blank=True)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)  
    user_type = models.CharField(max_length=50, choices=USER_TYPES,default=PENDING)
    avatar = ResizedImageField(default="avatars/default.png", upload_to='avatars/', null=True, blank=True)
    password_reset_count = models.IntegerField(null=True, blank=True, default=0)
    first_connexion = models.BooleanField(default=False)
    deletion_id = models.CharField(max_length=1000, blank=True, null=True)
    deletion_type = models.CharField(max_length=50,choices=USER_TYPES,blank=True,null=True)
    date_de_naissance = models.DateField(null=True)
    nationnalite = models.CharField(max_length=500)
    cni = models.CharField(max_length=500, null=True)
    ordre_des_medecins = models.CharField(max_length=255,null=True)
    pays_ordre_des_medecins = models.CharField(max_length=255,null=True)
    date_inscription_ordre = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    privacy = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # these field are required on registering
    REQUIRED_FIELDS = ['nom', 'prenom', 'telephone']
    
    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        app_label = "api"

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f'<User: {self.pk},email: {self.email}, user_type: {self.user_type}>'




class Classe(models.Model):
    nom = models.CharField(max_length=50)
    niveau = models.CharField(max_length=10)

    def __str__(self):
        return self.nom

class Eleve(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    risque_abandon = models.FloatField(null=True, blank=True)
    proba_reussite = models.FloatField(null=True, blank=True)
    # Champs supplémentaires
    application_mode = models.IntegerField()
    displaced = models.BooleanField(default=False)
    debtor = models.BooleanField(default=False)
    tuition_fees_up_to_date = models.BooleanField(default=False)
    gender = models.CharField(max_length=10)
    scholarship_holder = models.BooleanField(default=False)
    age_at_enrollment = models.IntegerField()
    curricular_units_1st_sem_enrolled = models.IntegerField()
    curricular_units_1st_sem_approved = models.IntegerField()
    curricular_units_1st_sem_grade = models.FloatField()
    curricular_units_2nd_sem_enrolled = models.IntegerField()
    curricular_units_2nd_sem_approved = models.IntegerField()
    curricular_units_2nd_sem_grade = models.FloatField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    