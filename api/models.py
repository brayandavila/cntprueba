from django.db import models

# Create your models here.

class Paciente(models.Model):
    documento = models.IntegerField(verbose_name='cedular')
    nombres = models.CharField(max_length=60, verbose_name='nombresr')
    apellidos = models.CharField(max_length=60, verbose_name='apellidosr')
    edad = models.IntegerField(verbose_name='edadr')
    direccion = models.CharField(max_length=45, verbose_name='direccionr')
    genero = models.CharField(max_length=40, verbose_name='generor')
    peso = models.FloatField(verbose_name='pesor')
    estatura = models.FloatField(verbose_name='estaturar')
    fuma = models.CharField(max_length=3, verbose_name='fumadorr')
    añosfumando = models.IntegerField(verbose_name='afumandor')
    dieta = models.CharField(max_length=3, verbose_name='dietar')
    rpe = models.FloatField(verbose_name='rpe')
    estado = models.CharField(max_length=10, verbose_name='estado')
    prioridad = models.FloatField(verbose_name='prioridad')
    riesgo = models.FloatField(verbose_name='riesgo')