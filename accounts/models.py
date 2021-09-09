from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from ubs.models import Cidade, Estado, Ubs

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email é obrigatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    motorista_ubs = models.BooleanField(default=False)
    estado = models.ForeignKey('ubs.Estado', models.CASCADE, blank=True, null=True)
    cidade = models.ForeignKey('ubs.Cidade', models.CASCADE, blank=True, null=True)
    ubs = models.ForeignKey('ubs.Ubs', on_delete=models.CASCADE, blank=True, null=True)
    localizacao = models.CharField(max_length=255)
    is_staff = models.BooleanField("membro", default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email

    class Meta:
        db_table = "usuario"
        managed = True

    objects = UsuarioManager() 