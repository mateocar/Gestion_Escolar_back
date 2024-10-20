# Sistema de Gestión Escolar

[![es](https://img.shields.io/badge/idioma-es-green)](https://github.com/mateocar/Gestion_Escolar_back/blob/main/README.md)
[![es](https://img.shields.io/badge/idioma-en-red)](https://github.com/mateocar/Gestion_Escolar_back/blob/main/README.en.md)
[![fr](https://img.shields.io/badge/idioma-fr-blue)](https://github.com/mateocar/Gestion_Escolar_back/blob/main/README.fr.md)

## Integrantes

- [Mateo Cardenas Osorio](https://github.com/mateocar)
- [Andres Navarro De la Hoz](https://github.com/eldelahoz)
- [Rina Plata Lopez](https://github.com/Rinaplata)

## Descripción del Proyecto

El Sistema de Gestión Escolar es una aplicación desarrollada para ayudar a las escuelas a manejar eficientemente la información de estudiantes, profesores, cursos y calificaciones. Este sistema proporciona una plataforma integral para la administración escolar, mejorando la comunicación y optimizando la gestión académica.

## Tecnología

- Django Rest Framework.
- PostgreSQL

## Uso

### Entorno virtual

1. **Creación del entorno**

```bash
python -m venv env
```

2. **Ejecutar**

| Sistema | Comando                  |
| ------- | ------------------------ |
| Windows | .env\Scripts\Activate    |
| Linux   | source .env/bin/activate |

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

`Note : Recordar estar en la misma ruta que esta el archivo requirements.txt`

> [!IMPORTANT]
> En caso de no querer usar PostgreSQL como motor de base de datos seguir los pasos de SQLite

<details>
<summary>PostgreSQL</summary>

1. **Archivos necesarios para PostgreSQL (LOCAL)**

   Si estas ejecutando una base de datos desde posgres tienes que agregar las variables en un archivo .env (si no tienes el archivo crearlo) y ponerle las siguientes variables:

   ```bash
        POSTGRESQL_NAME=<posgresql_database>
        POSTGRESQL_USER=<posgresql_user>
        POSTGRESQL_PASS=<postgresql_pass>
        POSTGRESQL_HOST=localhost
        POSTGRESQL_PORT=5432
        DEBUG=True
   ```

2. **Crear contenedor de postgres**

   En el archivo `docker-compose.yml` se encuentra configurada una imagen de postgresql-alpine para la creacion de la base de datos de manera local.
   Tener cuenta cambiar las siguientes variables de entorno:

```bash
- POSTGRES_PASSWORD=(Contraseña igual a la que se ponga en el archivo .pgpass)
- POSTGRES_USER=username(Usuario igual al que se ponga en el archivo .pgpass)
```

</details>

<details>
<summary>SQLite</summary>

1. **Cambiar Motor de base de datos en settings.py**

En el archivo settings.py ubicado en `gestion_escolar\settings.py` cambiar la siguiente parte de codigo

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

Por esta:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

</details>

### Estructura de la Base de Datos

1. **Usuarios (Users)**
2. **Estudiantes (Students)**
3. **Profesores (Teachers)**
4. **Cursos (Courses)**
5. **Calificaciones (Grades)**

## **Ruta de Swagger:**

## Arquitectura

![Arquitecutra](./Doc/img/Arquitectura%20Back%20Gestion%20Escolar.jpg)
