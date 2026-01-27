from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CarSerializer(serializers.HyperlinkedModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Car
        fields = ['name', 'user', 'color', 'price', 'id', 'url']

    def validate(self, data):
        price = data.get('price')
        if price is not None and price < 100:
            raise serializers.ValidationError('The price must be greater than 1000!')
        return data

class UserSerializer(serializers.HyperlinkedModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'cars', 'url']
