from django.http import JsonResponse

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view

from StudentApp.models import Student
from StudentApp.serializers import StudentSerializer


@api_view(['GET'])
def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_serializer = StudentSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)


@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
        try:
            student = Student.objects.create(
                code=request.data.get('code'),
                firstname=request.data.get('firstname'),
                lastname=request.data.get('lastname')
            )
            student.save()
            return JsonResponse({'message': "Student saved!"}, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse({'message': "Student not saved!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_student(request, code):
    if request.method == 'PUT':
        try:
            student = Student.objects.get(code=code)
            student.firstname = request.data['firstname']
            student.lastname = request.data['lastname']
            student.save()
            return JsonResponse({'message': 'Student updated successfully!'}, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse({'message': "Student not updated!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request, code):
    if request.method == 'DELETE':
        try:
            student = Student.objects.get(code=code)
            if student:
                student.delete()
            return JsonResponse({'message': 'Student deleted successfully!'})
        except Exception:
            return JsonResponse({'message': "Student does not exist!"}, status=status.HTTP_400_BAD_REQUEST)
