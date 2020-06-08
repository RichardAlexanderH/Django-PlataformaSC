from django.db import models

# Create your models here.

class Nivel(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return self.nivel 

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    Tel = models.CharField(max_length=10)
    pasword = models.CharField(max_length=20)
    Fecha_Nacimiento = models.DateField()
    id_nivel = models.ForeignKey(Nivel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'El nombre es %s y la contraseña es %s' %(self.nombre,self.pasword)

class logeados(models.Model):
    usuario = models.CharField(max_length=50)
    ingres = models.BooleanField()
    id_nivel = models.ForeignKey(Nivel, null=True, on_delete=models.CASCADE)
    hora_log = models.DateField()
