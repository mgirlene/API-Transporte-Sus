from django.db import models
from ubs.models import Ubs

class StatusAgendamento(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_status_agendamento")
    status = models.CharField(max_length=50)
    observacao = models.TextField(max_length=255)

    def _str_(self):
        return '{}'.format(self.id)

    class Meta:
        db_table='status_agendamento'
        verbose_name_plural = 'status_agendamentos'

class Agendamento(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_agendamento")
    ubs = models.ForeignKey(Ubs, on_delete=models.CASCADE)
    minha_localizacao = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    data = models.DateField()
    hora = models.TimeField()
    usuario = models.ForeignKey('accounts.CustomUsuario', on_delete=models.CASCADE)
    status = models.ForeignKey(StatusAgendamento, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.destino)

    class Meta:
        db_table='agendamento'
        verbose_name_plural = 'agendamentos'