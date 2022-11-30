from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from student.models import StudentTable
from student.serializers import studentSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all students
    if request.method == 'GET':
        students = StudentTable.objects.all()

        title = request.GET.get('StudentName', None)
        if title is not None:
            student = student.filter(title__icontains=title)

        student_serializer = studentSerializer(student, many=True)
        return JsonResponse(student_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = studentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = StudentTable.objects.all().delete()
        return JsonResponse({'message': '{} Students were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    # find student by pk (id)
    try:
        student = StudentTable.objects.get(pk=pk)
    except StudentTable.DoesNotExist:
        return JsonResponse({'message': 'Student does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET / PUT / DELETE tutorial
    if request.method == 'GET':
        student_serializer = studentSerializer(StudentTable)
        return JsonResponse(student_serializer.data)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student_serializer = studentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


""""
@api_view(['GET'])
def student_list_published(request):
    # GET all published students
    students = StudentTable.objects.filter(published=True)

    if request.method == 'GET':
        student_serializer = studentSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)
"""
