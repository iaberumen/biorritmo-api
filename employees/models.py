from django.db import models

# Create your models here.
class Employee(models.Model):
    curp = models.CharField(max_length=20,blank=True)
    rfc = models.CharField(max_length=20,blank=False)
    fecha_nacimiento = models.DateTimeField(blank=False)
    fecha_accidente = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'