from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from .forms import StudentForm, CourseForm


class StudentListView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students.html'
    success_url = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context


class CourseListView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses.html'
    success_url = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class StudentDetailView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        available_courses = Course.objects.exclude(students=student)
        return render(request, 'details.html', {'student': student, 'available_courses': available_courses})

    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        course_id = request.POST.get('course_id')
        if course_id:
            course = get_object_or_404(Course, id=course_id)
            student.courses.add(course)
            return redirect('details', student_id=student_id)
        return render(request, 'details.html', {'student': student})
