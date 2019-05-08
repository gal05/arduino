from django.db import models


class Data(models.Model):
    id = models.AutoField(primary_key=True)
    humedad = models.CharField(max_length=100)
    temperatura = models.CharField(max_length=100)
    rayos_v = models.CharField(max_length=100)
    sensor_lluvia = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = "data"

    def __str__(self):
        return self.humedad
