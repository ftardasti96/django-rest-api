#request the api and get the api back

from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer

# Create your views here.
class EmployeeList(APIView):

    #returns the list of all employees
    def get(self,request):
        my_employee = Employee.objects.all()
        serializer = EmployeeSerializer(my_employee, many=True)
        return Response(serializer.data)

    #to create a new employee
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


