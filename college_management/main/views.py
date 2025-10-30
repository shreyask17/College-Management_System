from django.shortcuts import render
from .models import Student, Attendance, Marks, Course, Teacher
from django.db.models import Avg, Count
from django.contrib import messages

def student_dashboard(request, student_id):
    student = Student.objects.get(id=student_id)
    attendance_records = Attendance.objects.filter(student=student)
    marks_records = Marks.objects.filter(student=student)
    return render(request, 'student_dashboard.html', {
        'student': student,
        'attendance_records': attendance_records,
        'marks_records': marks_records
    })

def teacher_dashboard(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    # All courses (unassigned + assigned to this teacher) so teacher can choose
    all_courses = Course.objects.all().order_by('name')
    # Only this teacher's courses for display where needed
    teacher_courses = Course.objects.filter(teacher=teacher)

    students = Student.objects.all()

    if request.method == 'POST':
        # Assign course to teacher
        if 'assign_course' in request.POST:
            course_id = request.POST.get('course_to_assign')
            if course_id:
                course = Course.objects.get(id=course_id)
                course.teacher = teacher
                course.save()
                messages.success(request, f"Course '{course.name}' assigned to {teacher.full_name}.")
                # refresh lists
                teacher_courses = Course.objects.filter(teacher=teacher)
        # Save Attendance
        elif 'attendance_submit' in request.POST:
            student_id = request.POST['student']
            course_id = request.POST['course']
            status = request.POST['status']
            Attendance.objects.create(
                student_id=student_id,
                course_id=course_id,
                date=request.POST['date'],
                status=status
            )
            messages.success(request, "Attendance saved.")
        # Save Marks
        elif 'marks_submit' in request.POST:
            student_id = request.POST['student']
            course_id = request.POST['course']
            marks_obtained = request.POST['marks_obtained']
            total_marks = request.POST['total_marks']
            grade = request.POST['grade']
            Marks.objects.create(
                student_id=student_id,
                course_id=course_id,
                marks_obtained=marks_obtained,
                total_marks=total_marks,
                grade=grade
            )
            messages.success(request, "Marks saved.")

    context = {
        'teacher': teacher,
        'courses': teacher_courses,
        'all_courses': all_courses,
        'students': students,
    }
    return render(request, 'teacher_dashboard.html', context)


def student_summary(request, student_id):
    student = Student.objects.get(id=student_id)
    total_classes = Attendance.objects.filter(student=student).count()
    attended_classes = Attendance.objects.filter(student=student, status='Present').count()
    attendance_percentage = (attended_classes / total_classes * 100) if total_classes > 0 else 0

    average_marks = Marks.objects.filter(student=student).aggregate(Avg('marks_obtained'))['marks_obtained__avg'] or 0

    context = {
        'student': student,
        'attendance_percentage': round(attendance_percentage, 2),
        'average_marks': round(average_marks, 2),
    }
    return render(request, 'student_summary.html', context)

def home(request):
    return render(request, 'home.html')