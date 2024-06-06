from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class AbstractModel(models.Model):
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
    class Meta:
        abstract = True



class GeneralSetting(AbstractModel):
    name = models.CharField(max_length=254, default='', blank=True, verbose_name='Name ',
                            help_text='This is val. of the Setting')
    description = models.CharField(max_length=254, default='', blank=True, verbose_name='Description ')
    parameters = models.CharField(max_length=254, default='', blank=True, verbose_name='Parameter ')



    def __str__(self):
        return f'General Settings: {self.name}'


    class Meta:
       verbose_name = 'General Setting'
       verbose_name = 'General Settings'
       ordering = ('name',)


class ImageSetting(AbstractModel):
   name = models.CharField(max_length=254, default='', blank=True, verbose_name='Name ',)
   description = models.CharField(max_length=254, default='', blank=True, verbose_name='Description ',)
   file = models.FileField(default='', blank=True, verbose_name='Image ',upload_to='images/')


   def __str__(self):
       return f'Image Settings: {self.name}'

   class Meta:
       verbose_name = 'Image Setting'
       verbose_name = 'Image Settings'
       ordering = ('name',)


class Skill(AbstractModel):
    order = models.IntegerField(default=0,verbose_name='Order ')
    name = models.CharField(max_length=254, default='', blank=True, verbose_name='Name ',
                            help_text='This is val. of the Setting')
    percentage = models.IntegerField( default=50, blank=True, verbose_name='Percentage ', validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f'Skill Settings: {self.name}'

    class Meta:
        verbose_name = 'Skill Setting'
        verbose_name = 'Skill Settings'
        ordering = ('order',)

class Experience(AbstractModel):
    company_name = models.CharField(max_length=254, default='', blank=True, verbose_name='Company Name ',)
    job_tittle = models.CharField(max_length=254, default='', blank=True, verbose_name='Job Tittle ',)
    job_location = models.CharField(max_length=254, default='', blank=True, verbose_name='Job Location ',)
    start_date = models.DateTimeField( verbose_name='Start Date ',default=None ,null=True ,blank=True)
    end_date = models.DateTimeField( verbose_name='End Date ',default=None ,null=True ,blank=True)
    def __str__(self):
        return f'Experience Settings: {self.company_name}'

    class Meta:
        verbose_name = 'Experience Setting'
        verbose_name = 'Experience Settings'
        ordering = ('start_date',)



class Education(AbstractModel):
    education_name = models.CharField(max_length=254, default='', blank=True, verbose_name='Education Name ',)
    education_lvl = models.CharField(max_length=254, default='', blank=True, verbose_name='Education Level ',)
    education_location = models.CharField(max_length=254, default='', blank=True, verbose_name='Education Location ',)
    start_date = models.DateTimeField( verbose_name='Start Date ',default=None ,null=True ,blank=True)
    end_date = models.DateTimeField( verbose_name='End Date ',default=None ,null=True ,blank=True)
    def __str__(self):
        return f'Education Settings: {self.education_name}'

    class Meta:
        verbose_name = 'Education Setting'
        verbose_name_plural = 'Education Settings'
        ordering = ('start_date',)



class SocialMedia(AbstractModel):
    order = models.IntegerField(default=0,verbose_name='Order ')
    link = models.CharField(max_length=254, default='', blank=True, verbose_name='Link ',)
    icon= models.CharField(max_length=254, default='', blank=True, verbose_name='Icon ',)
    def __str__(self):
        return f'Social Media Settings: {self.link}'

    class Meta:
        verbose_name = 'Social Media Setting'
        verbose_name_plural = 'Social Media Settings'
        ordering = ('order',)



class Document(AbstractModel):
    order = models.IntegerField(default=0,verbose_name='Order ')

    slug = models.SlugField(max_length=254, default='', blank=True, verbose_name='Slug Name ', )
    button_text =models.CharField(max_length=254, default='', blank=True, verbose_name='Button Text ',)
    file = models.FileField(default='', blank=True, verbose_name='Image ', upload_to='documents/')

    def __str__(self):
        return f'Document Settings: {self.slug}'

    class Meta:
        verbose_name = 'Document Setting'
        verbose_name = 'Document Settings'
        ordering = ('order',)
