from .views import prefixes_view
from django.urls import path



urlpatterns = [
    path("prefixes", prefixes_view, name="prefixes"),
]