from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from ubs.models import Ubs, Cidade, Estado


class EnderecoUser(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_enderecouser")
    estado = models.ForeignKey(Estado, models.CASCADE)
    cidade = models.ForeignKey(Cidade, models.CASCADE)
    localizacao = models.CharField(max_length=255)
    ubs = models.ForeignKey(Ubs, models.CASCADE)

    def __str__(self):
        return '{}'.format(self.localizacao)

    class Meta:
        db_table = 'endereco_user'
        verbose_name_plural = 'endereco_user'

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
    endereco = models.ForeignKey(EnderecoUser, models.CASCADE, blank=True, null=True)
    ubs = models.ForeignKey(Ubs, models.CASCADE, blank=True, null=True)
    is_staff = models.BooleanField("membro", default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email

    class Meta:
        db_table = "usuario"
        managed = True

    objects = UsuarioManager() 
    