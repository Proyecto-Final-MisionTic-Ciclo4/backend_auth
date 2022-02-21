# backend_auth

Authentication using DRF

I. CREACION DEL PROYECTO DJANGO:

Los pasos para poder crear un proyecto en Django (MTV) son los siguientes:

    1. Crear el ambiente de trabajo para volver independiente los paquetes ( python -m venv <env> )
    2. Entrar en el entorno virtual ( <env>\Scripts\activate )
    3. Para la creacion del proyecto Django se debe installar Django: ( pip install django )
    4. Se debe installar el framework rest ( pip install djangorestframework )
    5. Se debe crear el proyecto Django ( django-admin startproject <authProject> )
    6. Se indica el rest_framework que vamos a usar en ( proyecto.settings -> INSTALLED_APPS )
    7. Creacion de la aplicación Django ( django-admin startapp <appName> )
    8. Se indica la appName que vamos a usar en ( proyecto.settings -> INSTALLED_APPS )
    9. Ejecucion del Componente ( python manage.py runserver )

II. CREACION DEL SISTEMA DE AUTENTICACION JWT:

Los pasos para crear el Sistema de autenticacion JWT (instalacion) y conexión con django es:

    1. Se instala Simple JWT con el comando pip install djangorestframework-simplejwt
    2. Se debe permitir al sistema de autenticacion de Django que permita a Simple JWT el acceso a dicho sistema ( proyecto.settings -> )
        i.	REST_FRAMEWORK = { 'DEFAULT_PERMISSION_CLASSES': ( 'rest_framework.permissions.AllowAny', ), 'DEFAULT_AUTHENTICATION_CLASSES': ( 'rest_framework_simplejwt.authentication.JWTAuthentication', ) }
    3. Configurar los tockens
        i.	SIMPLE_JWT = { 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5), 'REFRESH_TOKEN_LIFETIME': timedelta(days=1), 'ROTATE_REFRESH_TOKENS': False, 'BLACKLIST_AFTER_ROTATION': True, 'UPDATE_LAST_LOGIN': False, 'ALGORITHM': 'HS256', 'USER_ID_FIELD': 'id', 'USER_ID_CLAIM': 'user_id', }

III. CONEXION CON LA BASE DE DATOS

Los pasos para conectarse con la base de datos son:

    1. Instalar el driver de la base de datos ( b.	pip install psycopg2 )
    2. Configurar la base de datos
        i. c.	DATABASES = {‘default': { 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': '', 'USER': '', 'PASSWORD': '', 'HOST': '', 'PORT': '5432', } }

IV. ESTRUCTURA DEL PROYECTO DJANGO

Se debe crear tres carpetas cada una con su archivo **init**.py: 1. Models -> Creacion de cada modelo dentro de esta carpeta 2. Serializers -> Creacion de los serializadores dentro de esta carpeta 3. Views -> Creacion de las vistas dentro de esta carpeta con su respectivo CRUD

V. MODELOS

Para lograr la persistencia es necesario utilizar el componente de la capa de datos bank_db, lo que implica la interacción entre la capa lógica, y la capa de datos

    1. Se usa el concepto de ORM -> a través de Modelos (Clases con atributos y métodos especiales), permite definir en la capa lógica la estructura con la que se almacenarán los datos
    2. Los ORM ayudan con un proceso llamado migraciones, permite crear el esquema en la base de datos correspondiente a la estructura ya definida
    3. Los ORM suelen definir una serie de métodos que facilitan la comunicación con la base de datos.
    4. Se crean los atributos y metodos a partir del diseño de la base de datos
    5. Se exportan y registran los modelos en el archivo __init__.py de la carpeta <authApp>/models
    6. Se deben registrar en <authApp>/admin.py
        i. from django.contrib import admin
        ii. from .models.categoria import Categoria
        iii. admin.site.register(User)
    7. Se indica cual sera el modelo para realizar la autenticacion en -> <authProject>/settings.py
        i. AUTH_USER_MODEL = 'ZarcoApp.User'

VI. MIGRACIONES

    1. Un proceso de migración consta de dos pasos, primero se crea una serie de archivos en la que se recolecta información de los modelos actuales y se definen las instrucciones de la migración, y un segundo paso en el que, con ayuda de los archivos previamente definidos, se crea el esquema en la base de datos
        i. python manage.py makemigrations
        ii. python manage.py migrate

VII. SERIALIZADORES

    1. Es por ello por lo que estas dos partes necesitan de una tercera parte llamada Controlador. Este hará las veces de intermediario, pues utilizará los modelos para responder las peticiones del usuario que llegan a través de las vistas.
    2. Un Serializer es un tipo de controlador cuya función es transformar información de un formato X a un formato Y y viceversa. el componente le brinda persistencia a la información usando una serie de modelos (que en el fondo son objetos instanciados), y por otra parte, el usuario se comunica con el componente a través de las vistas usando un formato como JSON o XML.
    3. Una de las herramientas más útiles es la creación de un Serializer a partir de un Modelo, esto ahorra gran parte del trabajo ya que con solo indicarle unos pocos parámetros Django REST se encarga del trabajo difícil
    4. Dado que Django REST permite crear Serializers a partir de modelos, en muchas ocasiones se puede presentar que dichos modelos tengan relaciones entre sí
    5. https://www.youtube.com/watch?v=B38aDwUpcFc

XIII. VIEWS

    1. https://www.youtube.com/watch?v=B38aDwUpcFc

IX. URL

X. SUPERUSER

    1. python manage.py createsuperuser
    2. select * from auth_user para mirar los superUsers

XI. PERMISOS

XII. Despliegue en Heroku entorno

    1. Archivo Procfile -> Esto le indica que debe desplegar en web a heroku usando gunicorn (proceso continuo) y las configuraciones de ejecucion estaran en la siguiente ruta
        i. web: gunicorn ZarcoApp.wsgi
    2. heroku -v
    3. heroku login
    4. heroku git:remote -a zarcos-app-be
    5. git add .
    6. git commit -m "Mensaje"
    7. git checkout master
    8. heroku config:set DISABLE_COLLECTSTATIC=1
    9. git push heroku master
    10. heroku config:set DJANGO_ALLOWED_HOSTS=https://zarcos-web-be.herokuapp.com/

XIII. DOKER - Clase 7

    1. Installar docker 
    2. Configurar doker
    3. Crear heroku ambiente
    3.1. Heroku login
    3.2. heroku container:login
    3.3. heroku container:push web - -app mision-tic-22-be-auth-ms <nombre app en heroku>
        heroku container:push mision-tic-22-be-auth-ms -a=authApp
    3.4. heroku container:release web --app mision-tic-22-be-auth-ms,
    4. Desplegado

XIV. FRONTEND

    1. Se necesita installar Vue Js

XV. PRUEBAS

{
"username": "juli",
"password": 54321,
"name": "Juliana",
"email": "cjaramillo"
}
