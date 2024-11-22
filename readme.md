# Gestion de Factures - Django Project

Ce projet est une application Django permettant de gérer des factures. Il inclut des fonctionnalités pour ajouter, afficher et gérer des factures au sein d'une base de données.

## Fonctionnalités

- **Afficher toutes les factures** : Voir une liste des factures existantes.
- **Ajouter une facture** : Ajouter une nouvelle facture via un formulaire.
- **Détails des factures** : Voir les informations détaillées pour chaque facture.
- **Supprimer ou modifier une facture** : Vous pouvez également modifier ou supprimer des factures existantes. Pour ce faire :
  - **Modifier une facture** : Allez sur la page de détail de la facture, puis cliquez sur le bouton pour la modifier. Vous pourrez alors changer les informations de la facture et enregistrer les modifications.
  - **Supprimer une facture** : Vous pouvez supprimer une facture directement depuis la page de détail de la facture en cliquant sur le bouton de suppression.

---

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :

- **Python 3.10 ou supérieur**
- **Django 4.0 ou supérieur**

---

## Installation

Suivez ces étapes pour configurer le projet sur votre machine locale.

1. Clonez le projet sur votre machine locale :

   ```bash
   git clone https://github.com/HoussainAT/PythonExam-Django.git
   cd exampython
   ```

2. Créez et activez un environnement virtuel :

   ```bash
   python -m venv env
   source env/bin/activate  # Sous Windows, utilisez `env\Scriptsctivate`
   ```

3. Installez les dépendances nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

4. Configurez la base de données dans le fichier `settings.py` de Django. Voici un exemple pour une base de données PostgreSQL :

   ```python
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }
   ```

5. Appliquez les migrations pour créer les tables dans la base de données :

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Lancez le serveur de développement :

   ```bash
   python manage.py runserver
   ```

   Vous pouvez maintenant accéder à l'application en ouvrant votre navigateur à l'adresse [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Utilisation

1. **Ajouter une facture** : Rendez-vous sur `/ajout_facture/` pour ajouter une nouvelle facture.
2. **Consulter les factures** : La page d'accueil `/` affiche la liste de toutes les factures existantes.

---

## Structure du projet

Voici une vue d'ensemble des fichiers et dossiers clés dans ce projet Django :

- `factureapp/`: Application principale pour la gestion des factures.
  - `models.py`: Définition des modèles de base de données.
  - `views.py`: Logique des vues pour gérer les factures.
  - `forms.py`: Formulaires pour l'ajout et la modification des factures.
- `templates/`: Contient les fichiers HTML pour l'interface utilisateur.
- `requirements.txt`: Liste des dépendances nécessaires pour le projet.

---

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.
