from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models

        # Votre code pour créer un super-utilisateur



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profil= models.CharField(max_length=50, unique=False)
    avatar = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.user.username