from django.contrib import admin
from .models import Course, Resource, Department, Like
# Register your models here.

admin.site.register(Course)
admin.site.register(Resource)
admin.site.register(Department)
admin.site.register(Like)