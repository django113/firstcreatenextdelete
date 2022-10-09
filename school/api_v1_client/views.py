from rest_framework import viewsets
from school.models import schoolStudentModel,schoolCourseModel
from .serializers import StudentSerializer,StudentCourseSerializer


class SchoolStudentViewset(viewsets.ModelViewSet):
    queryset=schoolStudentModel.objects.all()
    serializer_class=StudentSerializer

class SchoolCourseViewset(viewsets.ModelViewSet):
    queryset=schoolCourseModel.objects.all()
    serializer_class=StudentCourseSerializer


