from django.db import models

# Create your models here.

class Pais(models.Model):
	idpais = models.IntegerField(primary_key=True)
	nombrePais = models.CharField(max_length=100)


	def __str__(self):
		"""String for representing the Model object."""
		return self.nombrePais

class Periodista(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombreCompleto = models.CharField(max_length=200)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    pais = models.ForeignKey('Pais', on_delete=models.SET_NULL, null=True, blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        #return f'{self.id} ({self.title})'
        return self.nombreCompleto
