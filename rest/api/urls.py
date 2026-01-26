from app.views import CarListView, CarDetailView, UserListView, UserDetailView 
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
