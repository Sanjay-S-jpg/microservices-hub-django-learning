from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.shorten_url, name='shorten'),
    path('expand/<str:shortcode>/', views.expand_url, name='expand'),
    path('stats/<str:shortcode>/', views.stats, name='stats'),
]
