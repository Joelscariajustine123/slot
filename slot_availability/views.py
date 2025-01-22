from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Slot, Student
from .forms import CourseForm, StudentForm

def home(request):
    return render(request, 'home.html')

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            slot = student.slot
            if slot.total_students >= 18:
                return render(request, 'register_student.html', {'form': form, 'error': 'Slot is full.'})
            if slot.system_required >= 15 and student.system_required:
                return render(request, 'register_student.html', {'form': form, 'error': 'Systems are full. Bring laptops.'})
            student.save()
            slot.total_students += 1
            if student.system_required:
                slot.system_required += 1
            slot.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})

def student_list(request):
    students = Student.objects.select_related('course', 'slot')
    return render(request, 'student_list.html', {'students': students})

def slot_availability(request):
    slots = Slot.objects.all()
    return render(request, 'slot_availability.html', {'slots': slots})

# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'course_list.html', {'courses': courses})

def course_list(request):
    courses = Course.objects.all().prefetch_related('student_set')  # Prefetch related students
    return render(request, 'course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def remove_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('course_list')

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def remove_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    slot = student.slot
    if student.system_required:
        slot.system_required -= 1
    slot.total_students -= 1
    slot.save()
    student.delete()
    return redirect('student_list')
