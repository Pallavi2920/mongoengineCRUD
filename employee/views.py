from .models import *
from .serializers import *
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes, permission_classes


@api_view(['GET','POST','PUT', 'PATCH', 'DELETE'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def employee_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        id = pk
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        emp = Employee.objects.get(pk=id)
        emp.delete()
        return Response({'msg':'Data Deleted'})


# class EmployeeAPI(APIView):
#     # permission_classes = [IsAuthenticated]
#     # authentication_classes = [CustomAuthentication]
#
#     def get(self,request):
#         emp = Employee.objects.all()
#         serializer = EmployeeSerializer(emp,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         emp = EmployeeSerializer(data=request.data)
#         if emp.is_valid():
#             emp.save()
#             return Response(emp.data,status = status.HTTP_201_CREATED)
#         return Response(emp.errors,status = status.HTTP_400_BAD_REQUEST)
#
# class EmployeeDetailsBy_ID(APIView):
#
#     def get_object(self,id):
#         try:
#             return Employee.objects.get(id = id)
#         except Employee.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)
#
#     def get(self,request,id):
#         emp = self.get_object(id)
#         serializer = EmployeeSerializer(emp)
#         return Response(serializer.data)
#
#     def put(self,request,id):
#         emp = self.get_object(id)
#         serializer = EmployeeSerializer(emp, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,id):
#         emp = self.get_object(id)
#         emp.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
