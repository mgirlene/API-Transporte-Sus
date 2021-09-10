from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Estado(models.Model):
    id = models.AutoField(primary_key=True,db_column="id_estado")
    nome = models.CharField('nome', max_length=50)
    sigla = models.CharField('sigla', max_length=2)

    def __str__(self):
        return '{}'.format(self.nome)
    
    class Meta:
        db_table = 'estado'
        verbose_name_plural = 'estados'


class Cidade(models.Model):
    id = models.AutoField(primary_key=True,db_column="id_cidade")
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete= models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nome)
    
    class Meta:
        db_table = 'cidade'
        verbose_name_plural = 'cidades'


class Ubs(models.Model):
    id = models.AutoField(primary_key=True,db_column="id_ubs")
    nome = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete= models.CASCADE)
    endereco = models.CharField(max_length=255)
    cnes = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.nome)
    
    class Meta:
        db_table = 'ubs'
        verbose_name_plural = 'ubs'

class Motorista(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_motorista")
    usuario = models.ForeignKey('accounts.CustomUsuario', on_delete=models.CASCADE)
    ubs = models.ForeignKey(Ubs, on_delete=CASCADE)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        db_table = 'motorista'
        verbose_name_plural = 'motoristas'