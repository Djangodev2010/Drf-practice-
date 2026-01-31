from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from rest_framework import renderers
from app.views import api_root, CarViewSet, UserViewSet

car_list = CarViewSet.as_view({'get': 'list', 'post': 'create'})
car_detail = CarViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial-update', })

user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('', api_root),
    path('cars/', car_list, name='car-list'),
    path('car-detail/<int:pk>', car_detail, name='car-detail'),
    path('users/', user_list, name='user-list'),
    path('user-detail/<int:pk>', user_detail, name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)

