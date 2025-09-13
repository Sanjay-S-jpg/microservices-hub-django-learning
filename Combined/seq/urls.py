from django.urls import path, include
from django.http import JsonResponse
from . import views

def api_home(request):
    return JsonResponse({
        "message": "Welcome to the Student API",
        "endpoints": [
            "/api/students/",
            "/api/students/form/"
        ]
    })

urlpatterns = [
    path("students/", views.StudentListCreate.as_view(), name="student_list_create"),
    path("students/form/", views.student_form, name="student_form"),
    path("", api_home, name="api_home"),   # <-- handles /api/
]