#serializer's job is to convert our model into json 
#we should import serializer and model

from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields= '__all__'