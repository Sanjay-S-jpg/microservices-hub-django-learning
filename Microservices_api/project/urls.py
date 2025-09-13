from django.urls import path
from .views import numbers,primes,fibo,odd

urlpatterns = [
    path("numbers", numbers),
    path("primes", primes),
    path("fibo", fibo),
    path("odd", odd),
]
