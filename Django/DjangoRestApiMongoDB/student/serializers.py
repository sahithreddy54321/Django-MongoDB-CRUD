from rest_framework import serializers
from student.models import StudentTable


class studentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentTable
        fields = ('StudentID',
                  'StudentName',
                  'Age',
                  'DOB',
                  'Grade')
