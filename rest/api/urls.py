from app.views import CarListView, CarDetailView, UserListView, UserDetailView 
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    path('', views.api_root),
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
