from django.urls import path
from .views import AirplaneListCreateView, AirplaneUpdateDetailView

urlpatterns = [
    path("", AirplaneListCreateView.as_view(), name="airplane-list-create"),
    path("<int:id>", AirplaneUpdateDetailView.as_view(), name="airplane-update-detail")
]
