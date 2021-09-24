from django.db import models

class Cidade(models.Model):
    id = models.AutoField(primary_key=True,db_column="id_cidade")
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nome)
    
    class Meta:
        db_table = 'cidade'
        verbose_name_plural = 'cidades'


class Ubs(models.Model):
    id = models.AutoField(primary_key=True,db_column="id_ubs")
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    cnes = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete= models.CASCADE)
    motorista = models.ForeignKey('accounts.CustomUsuario', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nome)
    
    class Meta:
        db_table = 'ubs'
        verbose_name_plural = 'ubs'