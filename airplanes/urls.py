from django.urls import path
from .airplane_views.airplane_list_create_view import AirplaneListCreateView
from .airplane_views.airplane_update_detail_view import AirplaneUpdateDetailView
from .airplane_views.airplane_flights_view import AirplaneFlightsView

urlpatterns = [
    path("", AirplaneListCreateView.as_view(), name="airplane-list-create"),
    path("<int:id>", AirplaneUpdateDetailView.as_view(), name="airplane-update-detail"),
    path("<int:id>/flights", AirplaneFlightsView.as_view(), name="flight-list-spesific-airplane")
]
