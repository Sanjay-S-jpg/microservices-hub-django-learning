from django.urls import path,include
from .views import notes
from . import views


urlpatterns = [
    path("notes/", views.notes, name="notes"),
]