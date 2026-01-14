from django.urls import path
from .views import ReservationUpdateDetailView, ReservationListCreateView

urlpatterns = [
    path('', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('<int:id>', ReservationUpdateDetailView.as_view(), name='reservation-detail-update')
]
