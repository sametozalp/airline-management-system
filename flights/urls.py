from django.urls import path
from .views import FlightListCreateView, FlightUpdateDetailView

urlpatterns = [
    path('', FlightListCreateView.as_view(), name='flight-list-create'),
    path('<int:id>', FlightUpdateDetailView.as_view(), name='flight-detail-update')
]
