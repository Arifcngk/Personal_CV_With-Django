from django.shortcuts import render
from core.models import GeneralSetting ,ImageSetting ,Skill ,Experience


# Create your views here.

def index(request):
    site_tittle = GeneralSetting.objects.get(name='site_tittle').parameters
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameters
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameters
    home_banner_tittle = GeneralSetting.objects.get(name='home_banner_tittle').parameters
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameters
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameters
    about_me_footer = GeneralSetting.objects.get(name='about_me_footer').parameters


# Images
    header_logo = ImageSetting.objects.get(name='header_logo').file
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file


#Skill
    skills = Skill.objects.all().order_by('order')


#Experience

    experiences = Experience.objects.all()



    context = {
        'site_tittle': site_tittle,
        'site_keywords': site_keywords,
        'home_banner_name': home_banner_name,
        'home_banner_tittle': home_banner_tittle,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_me_footer': about_me_footer,
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        'skills': skills,
        'experiences': experiences


    }
    return render(request, 'index.html', context=context)
