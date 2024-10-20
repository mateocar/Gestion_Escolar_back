# School Management System

[![en](https://img.shields.io/badge/language-en-red)](https://github.com/mateocar/Gestion_Escolar_back/blob/main/README.en.md)
[![es](https://img.shields.io/badge/language-es-green)](https://github.com/mateocar/Gestion_Escolar_back/blob/main/README.md)
[![fr](https://img.shields.io/badge/language-fr-blue)](https://github.com/mateocar/Gestion_Escolar_back/blob/main/README.fr.md)

## Team Members

- [Mateo Cardenas Osorio](https://github.com/mateocar)
- [Andres Navarro De la Hoz](https://github.com/eldelahoz)
- [Rina Plata Lopez](https://github.com/Rinaplata)

## Project Description

The School Management System is an application developed to help schools efficiently manage information about students, teachers, courses, and grades. This system provides a comprehensive platform for school administration, improving communication and optimizing academic management.

## Technology

- Django Rest Framewok.
- PostgreSQL

## Usage

### Virtual environment

1. **Creating the environment**

```bash
python -m venv env
```

2. **Activate**

| System  | Command                  |
| ------- | ------------------------ |
| Windows | .env\Scripts\Activate    |
| Linux   | source .env/bin/activate |

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

`Note: Remember to be in the folder where the requirements.txt file is located`

> [!IMPORTANT]
> In case you do not want to use PostgreSQL as database engine follow the SQLite steps

<details>
<summary>PostgreSQL</summary>

1. **Necessary files for PostgreSQL (LOCAL)**

   If you are running a database from postgres you have to add the variables in a .env file (if you don't have the file create it) and put the following variables in it:

   ```bash
       POSTGRESQL_NAME=<posgresql_database>
       POSTGRESQL_USER=<posgresql_user>
       POSTGRESQL_PASS=<postgresql_pass>
       POSTGRESQL_HOST=localhost
       POSTGRESQL_PORT=5432
       DEBUG=True
   ```

2. **Create a PostgreSQL container**

   In the `docker-compose.yml` file, there is a configuration for a postgresql-alpine image for local database creation. Make sure to change the following environment variables:

```bash
- POSTGRES_PASSWORD=(Same password as in the .pgpass file)
- POSTGRES_USER=username(Same user as in the .pgpass file)
```

</details>

<details>
<summary>SQLite</summary>

1. **Change Database Engine in settings.py**

In the settings.py file located in `gestion_escolar\settings.py` change the following part of code

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

For this

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

</details>

### Database Structure

1. **Users**
2. **Students**
3. **Teachers**
4. **Courses**
5. **Grades**

## **Swagger Path:**

## Architecture

![Arquitecutra](./Doc/img/Arquitectura%20Back%20Gestion%20Escolar.jpg)
