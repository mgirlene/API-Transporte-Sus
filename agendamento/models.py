from django.db import models
from ubs.models import Ubs
from accounts.models import CustomUsuario

class Agendamento(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_agendamento")
    ubs = models.ForeignKey(Ubs, on_delete=models.CASCADE)
    minha_localizacao = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    data = models.DateField()
    hora = models.TimeField()
    usuario = models.ForeignKey('accounts.CustomUsuario', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        db_table='agendamento'
        verbose_name_plural = 'agendamentos'

class Status(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_status")
    nome = models.CharField(max_length=50)

    def _str_(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table='status'
        verbose_name_plural = 'status'

class StatusAgendamento(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_status_agendamento")
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    observacao = models.TextField(max_length=255)

    def _str_(self):
        return '{}'.format(self.id)

    class Meta:
        db_table='status_agendamento'
        verbose_name_plural = 'status_agendamentos'
