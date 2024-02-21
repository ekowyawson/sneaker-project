from django.urls import path
from .views import SneakerList, SneakerDetail

urlpatterns = [
  path("", SneakerList.as_view(), name="sneaker_list"),
  path("<int:pk>/", SneakerDetail.as_view(), name="sneaker_detail"),
]
