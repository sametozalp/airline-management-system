from django.urls import path
from .views import get_all, get_detail

urlpatterns = [
    path('get_all', get_all, name='get_all'),
    path('<int:id>', get_detail, name='get_detail')
]
