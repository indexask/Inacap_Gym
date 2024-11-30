from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images")
    url = URLField(blank=True)
    date = DateField(default=date.today)

    def __str__(self) -> str:
        return self.title
    
class Usuario(AbstractBaseUser):
    nombre = models.CharField(
        verbose_name='',
        max_length=30,
    )
    apellido = models.CharField(
        verbose_name='',
        max_length=30,
    )
    rut = models.CharField(
        verbose_name='',
        max_length=12,
        unique=True,
    )
    correo = models.EmailField(
        verbose_name='',
        max_length=70,
        unique=True,
    )
    usuario = models.CharField(
        verbose_name='',
        max_length=50,
        unique=True,
    )
    fecha_nacimiento = models.DateField(
        verbose_name='',
        max_length=50,
        unique=False,
        null=True,
    )
    activo = models.BooleanField(default=True)
    admin = models.BooleanField(default=False) 
    tecnico = models.BooleanField(default=False)

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['correo','rut']

    def get_full_name(self):
        return self.correo

    def get_short_name(self):
        return self.correo

    def has_perm(self, perm, obj=None):
        "El usuario tiene un permiso especifico?"
        return True

    def has_module_perms(self, app_label):
        "El usuario tiene permisos para ver la aplicacion 'app_label'?"
        return True

    @property
    def is_staff(self):
        "El usuario es miembro del staff?"
        return self.staff
