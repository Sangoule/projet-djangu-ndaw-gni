pip install django
django-admin startproject Toukil
django-admin startapp Toukil
cd Toukil
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
git 
git init
git add .
git commit -m ''
git branch -M main
git remote add origin https://github.com/Sangoule/application-de-reservation-de-vol.git
git push -u origin main
2-Remplir la base de données avec 3 Compagnies, 4 Vols (dont au moins un organisé par deux compagnies) 
et 3 Trajets (NB vous n’êtes pas obligés d’utiliser des vrais compagnies).
tout dabord on doit installer le module pylot pour l'image 
ensuite on specifie le chemin dans la quelle nos images vont etre stocker 
#####
Maintenant on crer notre superuser
avec la commande cd 
username dakantal 1
password dakantal 2 + chiffre prefere
nb en minuscule
#####
 dans notre admin.py on doit definir nos model pour qu'ils puisse s'afficher dans notre admin panel
 #####
 Enfin on ajoute les elements
 #!error str(self.prix)
 ## on affiche les donnees de la base au niveau des vues
#### Integration de template
done 
#### Pour creer une page on a besoin de sont url.py et d'une vues

### Deuxieme application
Pour chaque profil une application en haut y'a comment creer une application
    1. creer le projet startproject deja fait 
    2. django-admin startapp nomApplication
    2. ajoutez l'application aux niveau de setting du projet
### Table utilisateur
    1. on creer un model dans models.py de notre application
    2. On l'enregistre dans notre admin.py 
    3. on creer la migration avec(makemigrations)
    4. on lance la migration