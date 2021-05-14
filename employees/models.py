from django.db import models

# Create your models here.
class Employee(models.Model):
    curp = models.CharField(max_length=20,blank=True)
    rfc = models.CharField(max_length=20,blank=False)
    fecha_nacimiento = models.DateField(blank=False)
    fecha_accidente = models.DateField(null=True,blank=True,default=None)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
        constraints = [
                models.UniqueConstraint(fields=['rfc'], name='')
            ]
    
    def __str__(self):
        return self.name