from django.contrib import admin

# Register your models here.
from school.models import schoolStudentModel,schoolCourseModel

admin.site.register(schoolStudentModel)
admin.site.register(schoolCourseModel)