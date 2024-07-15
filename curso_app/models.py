from django.db import models

# Create your models here.


class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"


class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesor_id = models.ManyToManyField(Profesor)  # Relación Many to Many con Profesor

    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo})"


class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)  # Relación Foreign key

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut}) "

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, null=True, blank=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante_id = models.OneToOneField(Estudiante, on_delete=models.CASCADE)  # Relación One to One con Estudiante

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.dpto if self.dpto else ''}, {self.comuna}, {self.ciudad}, {self.region}"
