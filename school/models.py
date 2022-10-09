from django.db import models

# Create your models here.
class schoolStudentModel(models.Model):
    name=models.CharField(max_length=255)
    roll=models.IntegerField()
    city=models.CharField(max_length=255)


class schoolCourseModel(models.Model):
    student=models.ForeignKey(schoolStudentModel,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

    