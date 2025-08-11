from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class PowerStats(models.Model):
    intelligence = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1),MaxValueValidator(100)]
    )
    strength = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1),MaxValueValidator(100)]
    )
    speed = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1),MaxValueValidator(100)]
    )
    power = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1),MaxValueValidator(100)]
    )
    combat = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1),MaxValueValidator(100)]
    )
    durability = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1),MaxValueValidator(100)]
    )

class Biography(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    alter_egos = models.CharField(max_length=100, blank=True)
    aliases = models.JSONField(default=list, blank=True)
    place_of_birth = models.CharField(max_length=200, blank=True)
    first_appearance = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    alignment = models.CharField(max_length=20, blank=True)

class Appearance(models.Model):
    gender = models.CharField(max_length=20, blank=True)
    race = models.CharField(max_length=50, blank=True)
    height = models.JSONField(default=list, blank=True)
    weight = models.JSONField(default=list, blank=True)
    eye_color = models.CharField(max_length=30, blank=True)
    hair_color = models.CharField(max_length=30, blank=True)

class Work(models.Model):
    occupation = models.CharField(max_length=200, blank=True)
    base = models.CharField(max_length=200, blank=True)

class Connections(models.Model):
    group_affiliation = models.TextField(blank=True)
    relatives = models.TextField(blank=True)

class Image(models.Model):
    url = models.URLField(max_length=300, blank=True)

class Hero(models.Model):
    name = models.CharField(max_length=100, unique=True)
    powerstats = models.OneToOneField('PowerStats', on_delete=models.CASCADE)
    biography = models.OneToOneField('Biography', on_delete=models.CASCADE)
    appearance = models.OneToOneField('Appearance', on_delete=models.CASCADE)
    work = models.OneToOneField('Work', on_delete=models.CASCADE)
    connections = models.OneToOneField('Connections', on_delete=models.CASCADE)
    image = models.OneToOneField('Image', on_delete=models.CASCADE)
