from django.contrib import admin
from django.urls import path
from testing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dummy1/', views.dummy_numbers_1),
    path('dummy2/', views.dummy_numbers_2),
    path('numbers/', views.get_numbers),
]
