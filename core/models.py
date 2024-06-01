from django.db import models

# Create your models here.

class GeneralSettings(models.Model):
    name = models.CharField(max_length=254, default='', blank=True)
    description = models.CharField(max_length=254, default='', blank=True)
    parameters = models.CharField(max_length=254, default='', blank=True)

    updated_data = models.DateTimeField(
        auto_now=True,
        blank=True
    )
    created_data = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )
