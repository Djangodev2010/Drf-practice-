from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import *
from .serializers import *
from rest_framework import status, generics, permissions
from django.http import Http404
from django.contrib.auth.models import User
from .permissions import IsUserOrReadOnly
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import viewsets

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'users': reverse('user_list', request=request, format=format),
            'cars': reverse('car_list', request=request, format=format)
        }
    )

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """This viewset will handle both retrive and list actions that too read-only"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
