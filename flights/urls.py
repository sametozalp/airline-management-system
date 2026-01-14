from django.urls import path
from .flight_views.flight_list_create_view import FlightListCreateView
from .flight_views.flight_update_detail_view import FlightUpdateDetailView
from .flight_views.flight_reservations_view import FlightReservationsView

urlpatterns = [
    path('', FlightListCreateView.as_view(), name='flight-list-create'),
    path('<int:id>', FlightUpdateDetailView.as_view(), name='flight-detail-update'),
    path('<int:id>/reservations', FlightReservationsView.as_view(), name='spesific-reservations-of-flight')
]
