# **Projet 12 - EpicEvents**
*Développement d'un architecture back-end sécurisée en utilisant Django ORM*

### **Télécharger le projet et installer les dépendances**
**Sous Windows**
````
git clone https://github.com/YoucefCudder/projet12.git

cd projet12
python -m venv env
env\Scripts\activate

pip install -r requirements.txt
cd EpicEvents
````

### Créer une base de donnée PostgreSQL

Installer  [PostgreSQL](https://www.postgresql.org/download/). Suivre la [documentation](https://www.postgresql.org/)  pour installer une base de donnée via pgAdmin4

Créer un fichier .env au sein là où le fichier settings.py se situe pour mettre en place les variables d'environnement.

````
SECRET_KEY=django-insecure-4ixvg%9+wi(if7@uwcr%w_sag4y+vc5!zxghco_a3d6kq$o!
DATABASE_NAME= "votre nom de DB"
DATABASE_USER= "votre nom d'utilisateur postgre"
DATABASE_PASSWORD="votre mot de passe"
DATABASE_HOST=localhost
DATABASE_PORT=5432
````

###


### **Lancer le projet**


 1. `python3 manage.py createsuperuser`
 2. `python manage.py migrate`
 3. `python manage.py createsuperuser`
 4.  `python manage.py runserver`
 5.  Accès à l'interface d'administration django de l'application à l'URL  [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

