from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class MainDataBase(models.Model):
    nom = models.CharField(max_length=50)
    freqCard = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(25),
            MaxValueValidator(300)
        ]
    )


class ConfigDataBase(models.Model):
    freqCardTarget = models.IntegerField(blank=False, null=False, default=0)
    phraseMystere = models.CharField(max_length=150, default='')