from django.contrib import admin
from django.urls import path
from project import views

urlpatterns = [
        
        path('admin/', admin.site.urls),
        path('', views.home, name='home'),
        path('signup/', views.signup, name='signup'),
        path('product/<int:pk>/', views.product_detail, name='product_detail'),
        path('product/add/', views.product_create, name='product_create'),
        path('product/<int:pk>/edit/', views.product_update, name='product_update'),
        path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
        path('login/', views.custom_login, name='login'),
        path('logout/', views.custom_logout, name='logout'),
        
]