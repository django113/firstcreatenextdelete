from rest_framework import serializers
from school.models import *
class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    roll= serializers.IntegerField()
    city= serializers.CharField(max_length=100)
    course=serializers.ListField(child=serializers.CharField(max_length=100),write_only=True)



    class Meta:
        fields=('id','name','roll','city','course')

    # field level validation methods
    def validate_roll(self, value):
        if value is None and value >=100:
            raise serializers.ValidationError("seets full")
        return value

    def create(self,validate_data):

        # id=validate_data['id']
        name=validate_data['name']
        roll=validate_data['roll']
        city=validate_data['city']
        st=schoolStudentModel.objects.filter(name=name)
        if not st.exists():
            try:
                student=schoolStudentModel.objects.create(name=name,roll=roll,city=city)
                print("created",student)

                courses=validate_data['course']
                print("courses ",courses)
                for course in courses:
                    schoolCourseModel.objects.create(student=student,name=course) 
                    print("course create")

            except:
                pass
        else:
            try:
                st.delete()
                print('deleted')
                print("existed")
            except:
                pass


        # try:
        #     student_instance=schoolStudentModel.objects.get(name__iexact=name,roll__iexact=roll,city__iexact=city)
        
        #     course=schoolCourseModel.objects.get(student=student_instance,name=course)
        #     print("--------------",student_instance,course)

        # except:
        #     pass

       

        return validate_data

    def validate(self,data):
        id=data.get('id',None)
        print('=====',id)
        return data

        


class StudentCourseSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=200)

    def validate_name(self,value):
        if value is None:
            raise serilazers.ValidationError({'msg':"couse"})
        
        return value


    def create(self,validate_data):
        course=schoolCourseModel.objects.create(**validate_data)
        # try:
        #     student=schoolStudentModel.objects.create(**validate_data)
        #     print("created")
        # except:
        #     print("existed")
        #     student=schoolStudentModel.objects.filter(id=student.id)

        # courses=validate_data['name']
        # print("courses ",courses)

        return course
            


