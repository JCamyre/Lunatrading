from django.db import models

# Create your models here.


class Stat(models.Model):

    champion = models.CharField(max_length=20)
    kda = models.FloatField()

    def __str__(self):
        return f"{self.champion}: {self.kda}"
