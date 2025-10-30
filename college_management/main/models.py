from django.db import models
from django.contrib.auth.models import User

# Teacher model
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.full_name
    
# Course model
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    duration = models.IntegerField()
    topic = models.CharField(max_length=100)  # changed from 'subject' to 'topic'
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True, related_name="courses")

    def __str__(self):
        return self.name


# Subject model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.course.name})"

# Student model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')])
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.roll_no})"

# Attendance model
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.full_name} - {self.course.name} ({self.date})"

# Marks model
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.full_name} - {self.course.name} ({self.marks_obtained}/{self.total_marks})"
