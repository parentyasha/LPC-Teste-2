from django.db import models

class Agenda(models.Model):
    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    usuario = models.CharField('Quem é o usuario', max_length=128)
    data_compromisso = models.DateField("Data do Compromisso", blank=True,null=True)
    tipo_compromisso = models.CharField('Tipo de Compromisso:', max_length=128)
    tipo_Agenda = models.BooleanField('Agenda Privada')

    def __str__(self):
        return self.tipo_compromisso

class Agenda_Institucional(models.Model):
    data_feriado = models.DateField("Data do Feriado", blank=True,null=True)
    data_fim = models.DateField("Data do Fim do Feriado", blank=True,null=True)
    tipo_feriado = models.CharField('Tipo de Feriado:', max_length=128)

    def __str__(self):
        return self.tipo_feriado