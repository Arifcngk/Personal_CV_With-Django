from django.contrib import admin
from core.models import *


# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameters', 'updated_data', 'created_data']
    search_fields = ['id', 'name', 'description', 'parameters', 'updated_data', 'created_data']
    list_editable = ['name', 'description', 'parameters']

    class Meta:
        model = GeneralSetting


@admin.register(ImageSetting)
class ImageSetting(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_data', 'created_data']
    search_fields = ['id', 'name', 'description', 'file', 'updated_data', 'created_data']
    list_editable = ['name', 'description', 'file']

    class Meta:
        model = ImageSetting


@admin.register(Skill)
class Skill(admin.ModelAdmin):
    list_display = ['id', 'name', 'order', 'percentage','updated_data', 'created_data']
    search_fields = ['name']
    list_editable = ['name', 'order', 'percentage']

    class Meta:
        model = Skill


@admin.register(Experience)
class Experience(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_tittle', 'job_location','start_date','end_date','updated_data', 'created_data']
    search_fields = ['company_name']
    list_editable = ['company_name', 'job_tittle', 'job_location', 'start_date']

    class Meta:
        model = Experience


@admin.register(Education)
class Education(admin.ModelAdmin):
    list_display = ['id', 'education_name', 'education_lvl', 'education_location','start_date','end_date','updated_data', 'created_data']
    search_fields = ['education_name']
    list_editable = ['education_name', 'education_lvl', 'education_location', 'start_date']

    class Meta:
        model = Education




@admin.register(SocialMedia)
class SocialMedia(admin.ModelAdmin):
    list_display = ['id', 'order', 'link', 'icon',]
    search_fields = ['link']
    list_editable = ['order', 'link', 'icon']

    class Meta:
        model = SocialMedia





@admin.register(Document)
class Document(admin.ModelAdmin):
    list_display = ['id', 'slug','order', 'button_text', 'file',]
    search_fields = ['slug']
    list_editable = ['order', 'button_text', 'file','slug']

    class Meta:
        model = Document
