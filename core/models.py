from django.db import models


# Create your models here.

class GeneralSetting(models.Model):
    name = models.CharField(max_length=254, default='', blank=True, verbose_name='Name ',
                            help_text='This is val. of the Setting')
    description = models.CharField(max_length=254, default='', blank=True, verbose_name='Description ')
    parameters = models.CharField(max_length=254, default='', blank=True, verbose_name='Parameter ')

    updated_data = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='Updated Date '
    )
    created_data = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='Created Date '
    )

    def __str__(self):
        return f'General Settings: {self.name}'


class Meta:
    verbose_name = 'General Setting'
    verbose_name = 'General Settings'
    ordering = ('name',)
