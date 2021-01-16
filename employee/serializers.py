from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import *


class EmployeeSerializer(DocumentSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
