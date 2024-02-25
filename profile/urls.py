from django.urls import path
from profile.views import ProfileCreateView, ProfileDetailView, ProfileDeleteView, ProfileUpdateView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('details/', ProfileDetailView.as_view(), name='profile_detail'),
    path('delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('update/', ProfileUpdateView.as_view(), name='profile_update'),
]