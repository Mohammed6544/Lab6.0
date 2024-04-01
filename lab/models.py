from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=10, primary_key=True)

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    gpa = models.FloatField(max_length=3)
    courses = models.ManyToManyField(Course, related_name='students')