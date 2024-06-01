from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
def contact_form():
    context={
        'success': True,
        'message': 'Your contact form has been submitted',
    }
    return JsonResponse(context)


def contact(request):
    return render(request, 'contact.html')