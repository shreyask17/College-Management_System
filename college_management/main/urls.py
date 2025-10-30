from django.urls import path
from . import views

urlpatterns = [
    path('student/<int:student_id>/', views.student_dashboard, name='student_dashboard'),
    path('teacher/<int:teacher_id>/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/<int:student_id>/summary/', views.student_summary, name='student_summary'),
]
