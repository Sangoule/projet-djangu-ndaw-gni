from django.urls import path
from . import views


urlpatterns = [
    path('',views.trajects, name="trajects"),
    path('login',views.login_view, name="login"),
    path('profile',views.profile, name="profile"),
    path('register',views.register, name="register"),
    path('vols',views.vols, name='vols'),
    path('compagnies',views.compagnies, name='compagnies'),
    path('volsdetails/<str:id>',views.volsdetails, name='volsdetails'),
    path('modif_comp/<str:id>',views.modif_comp, name='modif_comp'),
    path('compagnie_update/<str:id>',views.compagnie_update, name='compagnie_update'),
    path('trajects',views.trajects, name='trajects'),
    path('vol_delete/<str:id>',views.del_vol, name='vol_delete'),    
]