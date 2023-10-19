
from . import views
from . import predictions
from django.contrib import admin
from django.urls import include, path
from .eleves import eleve_list, eleve_detail, eleve_create, eleve_update, eleve_delete
from .classe import classe_list, classe_detail, classe_create, classe_update, classe_delete


urlpatterns = [
    path('',views.index, name="index"), 
    path('login',views.login_view, name="login"),
    path('donnes', views.donnes, name="donnes"),
    path('predictions', views.predictions, name="predictions"),
    path('register',views.register, name="register"),
    path('logout',views.logout_view, name="logout"),
    path('register_user_profil',views.register_user_profil, name="register_user_profil"),
    path('user-list',views.user_list, name="user-list"),
    path('edit_profile/<str:idUser>',views.edit_profile, name="edit-profile"),
    path('delete-user/<int:idUser>',views.delete_user, name="delete-user"),
    path('create-user',views.register_user_profil, name="create-user"),
    path('listeFormation', views.listeFormation, name="listeFormation"),
    path('listeEleves', views.listeEleves, name="listeEleves"),
    path('predictAll', predictions.getAllprediction, name="predictAll"),
    path('predict/<int:id>', predictions.getOnePrediction, name="predict"),
    path('predictStudent', predictions.predire, name="predictStudent"),

    path('classes/', views.liste_classes, name='liste_classes'),
    path('classes/<int:classe_id>/', views.liste_eleves_par_classe, name='liste_eleves_par_classe'),
]