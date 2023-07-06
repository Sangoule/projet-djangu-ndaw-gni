
from . import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="index"), 
    path('login',views.login_view, name="login"),
    path('register',views.register, name="register"),
    path('logout',views.logout_view, name="logout"),
    path('register_user_profil',views.register_user_profil, name="register_user_profil"),
    path('user-list',views.user_list, name="user-list"),
    path('edit_profile/<str:idUser>',views.edit_profile, name="edit-profile"),
    path('delete-user/<int:idUser>',views.delete_user, name="delete-user"),
    path('create-user',views.register_user_profil, name="create-user"),
]