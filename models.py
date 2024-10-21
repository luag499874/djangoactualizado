from pro_gol.db import models

# Create your models here.
from django.db import models

class videos(models.model):
    id = models.IntegerField(primary_key=True)
    pregunta1 = models.charField(max_length=100)
    pregunta2 = models.charField(max_length=100)

class Meta:
        db_table="usuarios"

    class videos(models.model):
        id = models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length=100)
        nomina = models.CharField(max_length=100)

    class Meta:
        db_table = "usuarios_videos"

    class videos(models.model):
    id = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=100)
    video = models.CharField(max_length=100)

    class Meta:
        db_table = "videos"

    class videos(models.model):
    id = models.IntegerField(primary_key=True)
    video = models.CharField(max_length=100)
    nombre_video = models.CharField(max_length=100)
    extension = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=100)