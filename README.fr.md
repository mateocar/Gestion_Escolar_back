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
python -m venv .env
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

4. **Fichiers nécessaires pour PostgreSQL (LOCAL)**

   Si vous exécutez une base de données PostgreSQL, vous devez ajouter les fichiers au chemin suivant selon votre système d'exploitation

| Système | Nom du fichier   | Chemin du fichier                                                                    |
| ------- | ---------------- | ------------------------------------------------------------------------------------ |
| Windows | .pg_service.conf | %APPDATA%\postgresql\\.pg_service.conf (SI la carpeta postgresql no existe, crearla) |
| Linux   | .pg_service.conf | ~/.pg_service.conf (Directorio local)                                                |

4. **Créer un conteneur PostgreSQL**

   Le fichier `docker-compose.yml` contient une configuration pour une image postgresql-alpine pour la création de la base de données en local. Veuillez modifier les variables d'environnement suivantes :

```bash
- POSTGRES_PASSWORD=(Same password as in the .pgpass file)
- POSTGRES_USER=username(Same user as in the .pgpass file)
```

### Structure de la Base de Données

1. **Utilisateurs**
2. **Étudiants**
3. **Enseignants**
4. **Cours**
5. **Notes**

## **Chemin Swagger :**

## Architecture

![Arquitecutra](./Doc/img/Arquitectura%20Back%20Gestion%20Escolar.jpg)
