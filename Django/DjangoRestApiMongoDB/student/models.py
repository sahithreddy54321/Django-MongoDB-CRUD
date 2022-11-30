from django.db import models


class StudentTable(models.Model):
    StudentID = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=500)
    Age = models.IntegerField()
    DOB = models.DateField()
    Grade = models.CharField(max_length=500)
