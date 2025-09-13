import requests
from django.http import JsonResponse
from urllib.parse import urlparse

def numbers(request):
    urls = request.GET.getlist("url")  # fetch all ?url= params
    numbers_set = set()

    for u in urls:
        try:
            # Validate URL
            result = urlparse(u)
            if all([result.scheme, result.netloc]):
                # Timeout to avoid slow response (>0.5s ignored)
                resp = requests.get(u, timeout=0.5)  
                if resp.status_code == 200:
                    data = resp.json()
                    nums = data.get("numbers", [])
                    numbers_set.update(nums)
        except Exception:
            continue  # skip slow/invalid URLs

    merged_numbers = sorted(numbers_set)

    return JsonResponse({"numbers": merged_numbers})

def primes(request):
    return JsonResponse({"numbers": [2, 3, 5, 7, 11, 13, 17, 19, 23]})

def fibo(request):
    return JsonResponse({"numbers": [1, 2, 3, 5, 8, 13, 21]})

def odd(request):
    return JsonResponse({"numbers": [1, 3, 5, 7, 9, 11, 13, 15]})