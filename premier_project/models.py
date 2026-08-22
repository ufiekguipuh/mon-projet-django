from django.db import models

class Station(models.Model):
    nom = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    en_garde = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
