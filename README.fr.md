# Système de Gestion Scolaire

[![fr](https://img.shields.io/badge/langue-fr-blue)](https://github.com/mateocar/Gestion_Escolar_back/blob/main/README.fr.md)
[![en](https://img.shields.io/badge/langue-en-red)](https://github.com/mateocar/Gestion_Escolar_back/blob/main/README.en.md)
[![es](https://img.shields.io/badge/langue-es-green)](https://github.com/mateocar/Gestion_Escolar_back/blob/main/README.md)

## Membres de l'équipe

- [Mateo Cardenas Osorio](https://github.com/mateocar)
- [Andres Navarro De la Hoz](https://github.com/eldelahoz)
- [Rina Plata Lopez](https://github.com/Rinaplata)

## Description du Projet

Le Système de Gestion Scolaire est une application développée pour aider les écoles à gérer efficacement les informations concernant les élèves, les enseignants, les cours et les notes. Ce système fournit une plateforme complète pour l'administration scolaire, améliorant la communication et optimisant la gestion académique.

## Technologie

- Django Rest Framework.
- PostgreSQL

## Utilisation

### Environnement virtuel

1. **Créer l'environnement**

```bash
python -m venv env
```

2. **Activer**

| Système | Commande                 |
| ------- | ------------------------ |
| Windows | .env\Scripts\Activate    |
| Linux   | source .env/bin/activate |

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

`Note : N'oubliez pas de vous placer dans le dossier où se trouve le fichier requirements.txt`

> [!IMPORTANT]
> Si vous ne voulez pas utiliser PostgreSQL comme moteur de base de données, suivez les étapes de SQLite

<details>
<summary>PostgreSQL</summary>

1. **Fichiers nécessaires pour PostgreSQL (LOCAL)**

   Si vous exécutez une base de données depuis Postgres, vous devez ajouter les variables dans un fichier .env (si vous n'avez pas le fichier, créez-le) et y mettre les variables suivantes :

   ```bash
       POSTGRESQL_NAME=<posgresql_database>
       POSTGRESQL_USER=<posgresql_user>
       POSTGRESQL_PASS=<postgresql_pass>
       POSTGRESQL_HOST=localhost
       POSTGRESQL_PORT=5432
       DEBUG=True
   ```

2. **Créer un conteneur PostgreSQL**

   Le fichier `docker-compose.yml` contient une configuration pour une image postgresql-alpine pour la création de la base de données en local. Veuillez modifier les variables d'environnement suivantes :

```bash
- POSTGRES_PASSWORD=(Same password as in the .pgpass file)
- POSTGRES_USER=username(Same user as in the .pgpass file)
```

</details>

<details>
<summary>SQLite</summary>

1. **Changer le moteur de base de données sur settings.py**

Dans le fichier settings.py situé à `gestion_escolar\settings.py` cchanger la partie suivante du code

```py
...
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRESQL_NAME'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASS'),
        'HOST': env('POSTGRESQL_HOST'),
        'PORT': env('POSTGRESQL_PORT'),
    }
}
...
```

Pour cette code:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

</details>

### Structure de la Base de Données

1. **Utilisateurs**
2. **Étudiants**
3. **Enseignants**
4. **Cours**
5. **Notes**

## **Chemin Swagger :**

## Architecture

![Arquitecutra](./Doc/img/Arquitectura%20Back%20Gestion%20Escolar.jpg)
