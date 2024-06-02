from django.shortcuts import render
from core.models import GeneralSetting


# Create your views here.

def index(request):
    site_tittle = GeneralSetting.objects.get(name='site_tittle').parameters
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameters
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameters
    home_banner_tittle = GeneralSetting.objects.get(name='home_banner_tittle').parameters
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameters
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameters
    about_me_footer = GeneralSetting.objects.get(name='about_me_footer').parameters





    context = {
        'site_tittle': site_tittle,
        'site_keywords': site_keywords,
        'home_banner_name': home_banner_name,
        'home_banner_tittle': home_banner_tittle,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_me_footer': about_me_footer,

    }
    return render(request, 'index.html', context=context)
