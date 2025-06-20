from django.db import models

# Create your models here.
class Candidato(models.Model):
    class EstadoEnum(models.TextChoices):
        RECLUTA = 'Reclutamiento', 'Reclutamiento'
        CONTRAT = 'Contratacion', 'Contratacion'
    estado = models.CharField(
        max_length=20,
        choices=EstadoEnum.choices,
        default=EstadoEnum.RECLUTA,
        null=True,
    )
    nombre = models.CharField(max_length=100,)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    rh = models.CharField(max_length=3, blank=True, null=True)
    ciudad_expedicion = models.CharField(max_length=100, blank=True, null=True)
    ciudad_nacimiento = models.CharField(max_length=100, blank=True, null=True)
    ciudad_domicilio = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

class OfertaLaboral(models.Model):
    cargo = models.CharField(max_length=100)
    cliente = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.cargo

    class Meta:
        verbose_name = "Oferta Laboral"
        verbose_name_plural = "Ofertas Laborales"

class Postulacion(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    oferta_laboral = models.ForeignKey(OfertaLaboral, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidato.nombre} - {self.oferta_laboral.cargo}"

    class Meta:
        verbose_name = "Postulación"
        verbose_name_plural = "Postulaciones"

class OrdenDeContratacion(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    postulacion = models.ForeignKey(Postulacion, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    examenes = models.FileField(upload_to='examenes/', blank=True, null=True)

    def __str__(self):
        return f"Orden de Contratación: {self.candidato.nombre} - {self.oferta_laboral.cargo}"

    class Meta:
        verbose_name = "Orden de Contratación"
        verbose_name_plural = "Órdenes de Contratación"