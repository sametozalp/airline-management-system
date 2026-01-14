from django.urls import path
# from .views import ReservationUpdateDetailView, ReservationListCreateView
from .reservation_views.reservation_list_create_view import ReservationListCreateView
from .reservation_views.reservation_update_detail_view import ReservationUpdateDetailView

urlpatterns = [
    path('', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('<int:id>', ReservationUpdateDetailView.as_view(), name='reservation-detail-update')
]

