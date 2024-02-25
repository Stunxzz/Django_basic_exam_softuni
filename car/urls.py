from django.urls import path
from car.views import CatalogView, CarCreateView, CarDetailView, CarDeleteView, CarUpdateView
urlpatterns = [
    path('catalogue/',CatalogView.as_view(), name='catalogue'),
    path('create/', CarCreateView.as_view(), name='create_car'),
    path('<int:pk>/details', CarDetailView.as_view(), name='car_detail'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    path('<int:pk>/edit/', CarUpdateView.as_view(), name='car_edit'),
]