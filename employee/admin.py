from django.contrib import admin
from . models import *
from django_mongoengine import mongo_admin  as admin

admin.site.register(Employee)

# Register your models here.
