from django.urls import path
from .views import get_all

urlpatterns = [
    path('get_all', get_all, name='get_all')
]
