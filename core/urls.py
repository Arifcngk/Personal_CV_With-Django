from django.urls import path
from .views import index, contact  # Değişiklik burada

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
]
