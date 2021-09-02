from django.db import models

class Estado(models.Model):
    id = models.AutoField(primary_key=True,db_column="id_estado")
    nome = models.TextField('nome', max_length=50)
    sigla = models.TextField('sigla', max_length=2)

    def __str__(self):
        return '{}'.format(self.nome)
    
    class Meta:
        db_table = 'estado'
        verbose_name_plural = 'estados'


class Cidade(models.Model):
    id = models.AutoField(primary_key=True,db_column="id_cidade")
    nome = models.TextField('nome', max_length=50)
    estado = models.ForeignKey("ubs.Estado", on_delete= models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nome)
    
    class Meta:
        db_table = 'cidade'
        verbose_name_plural = 'cidades'


class Ubs(models.Model):
    id = models.AutoField(primary_key=True,db_column="id_ubs")
    nome = models.TextField('nome', max_length=50)
    cidade = models.ForeignKey("ubs.Cidade", on_delete= models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nome)
    
    class Meta:
        db_table = 'ubs'
        verbose_name_plural = 'ubs'


     
