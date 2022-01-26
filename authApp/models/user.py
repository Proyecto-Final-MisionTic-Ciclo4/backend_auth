from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
            """ Manager para crear el perfil de usuario """
            if not username:
                raise ValueError('Es requerido que tener un usuario')
            user = self.model(username = username)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, username, password): # Comando en la terminal python manage.py createsuperuser
        """ Manager para crear el perfil del super usuario de Django"""
        user = self.create_user(
            username  = username,
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', unique=True, max_length=20)
    password = models.CharField('Password', max_length=256)
    name = models.CharField('Name', max_length=50)
    email = models.CharField('Email', max_length=100, unique=True)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager() # se enlaza con la clase manager
    USERNAME_FIELD = 'username' # es el que va a usar para generar los tockens