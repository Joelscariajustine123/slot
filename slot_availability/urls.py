from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_student, name='register_student'),
    path('students/', views.student_list, name='student_list'),
    path('slots/', views.slot_availability, name='slot_availability'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/remove/<int:course_id>/', views.remove_course, name='remove_course'),
    path('students/update/<int:student_id>/', views.update_student, name='update_student'),
    path('students/remove/<int:student_id>/', views.remove_student, name='remove_student'),
]
