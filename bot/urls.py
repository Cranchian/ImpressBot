from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import receive_message, display

app_name = 'bot'

urlpatterns = [
    path('webhooks/joke/', csrf_exempt(receive_message)),
    path('', display, name="display")
]
