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

- Django rest v.
- PostgreSQL

## Uso

### Entorno virtual

1. **Creación del entorno**

```bash
python -m venv .env
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

`Nota: Recordar estar ubicado en la carpeta que este el archivo requirements.txt`

4. **Archivos necesarios para PostgreSQL (LOCAL)**

   Si estas ejecutando una base de datos desde posgres tienes que agregar los archivos a la siguiente ruta dependiendo de tu sistema operativo

| Sistema | Nombre Archivo   | Ruta Archivo                                                                         |
| ------- | ---------------- | ------------------------------------------------------------------------------------ |
| Windows | .pg_service.conf | %APPDATA%\postgresql\\.pg_service.conf (SI la carpeta postgresql no existe, crearla) |
| Linux   | .pg_service.conf | ~/.pg_service.conf (Directorio local)                                                |

4. **Crear contenedor de postgres**

   En el archivo `docker-compose.yml` se encuentra configurada una imagen de postgresql-alpine para la creacion de la base de datos de manera local.
   Tener cuenta cambiar las siguientes variables de entorno:

```bash
- POSTGRES_PASSWORD=(Contraseña igual a la que se ponga en el archivo .pgpass)
- POSTGRES_USER=username(Usuario igual al que se ponga en el archivo .pgpass)
```

### Estructura de la Base de Datos

1. **Usuarios (Users)**
2. **Estudiantes (Students)**
3. **Profesores (Teachers)**
4. **Cursos (Courses)**
5. **Calificaciones (Grades)**

## **Ruta de Swagger:**

## Arquitectura

![Arquitecutra](./Doc/img/Arquitectura%20Back%20Gestion%20Escolar.jpg)
