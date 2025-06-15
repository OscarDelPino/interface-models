from django.urls import path
from .views import whatsapp_webhook

app_name = 'crm_test'

urlpatterns = [
    path('webhook/', whatsapp_webhook, name='webhook'),
]
