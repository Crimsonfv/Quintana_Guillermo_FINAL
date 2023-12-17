from django.db import models

# Create your models here.

class Instituciones(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Inscritos(models.Model):
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    FechaDeInscripcionYHora = models.DateField()
    Estado = models.CharField(max_length=50)
    Institucion = models.ForeignKey('Instituciones', models.DO_NOTHING, db_column='Institucion')
    Observaciones = models.TextField(blank=True, null=True)
