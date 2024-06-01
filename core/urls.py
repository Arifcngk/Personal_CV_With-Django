from django.urls import path
from .views import index  # Değişiklik burada

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
]
