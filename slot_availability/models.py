from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Slot(models.Model):
    time_range = models.CharField(max_length=50)
    days = models.CharField(max_length=100)
    total_students = models.IntegerField(default=0)
    system_required = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.time_range} - {self.days}"

class Student(models.Model):
    gcard_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    system_required = models.BooleanField(default=False)

    def __str__(self):
        return self.name
