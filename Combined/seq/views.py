from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Student
from .forms import StudentSerializer
from .forms import StudentForm

# ---- REST API View ----
class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# ---- HTML Form View ----
def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list_create")  # redirect to API after save
    else:
        form = StudentForm()
    return render(request, "student.html", {"form": form})
