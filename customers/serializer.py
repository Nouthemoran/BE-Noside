from rest_framework import serializers
from .models import Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields  = ['custId', 'name', 'email', 'phoneNumber', 'status']