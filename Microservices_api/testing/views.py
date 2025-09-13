from django.http import JsonResponse
import time

# This acts like our "mock" JSON API but inside Django
def dummy_numbers_1(request):
    return JsonResponse({"numbers": [1, 3, 5, 7, 9, 1, 5]})

def dummy_numbers_2(request):
    return JsonResponse({"numbers": [2, 4, 6, 8, 10, 3, 7]})

# The main API /numbers
def get_numbers(request):
    start_time = time.time()

    # Instead of fetching external URLs, we "call" our own dummy endpoints
    urls = [
        "http://localhost:8000/dummy1/",
        "http://localhost:8000/dummy2/"
    ]

    import requests

    all_numbers = []
    for url in urls:
        try:
            resp = requests.get(url, timeout=2)
            if resp.status_code == 200:
                data = resp.json()
                all_numbers.extend(data.get("numbers", []))
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    # Remove duplicates & sort
    result = sorted(list(set(all_numbers)))

    execution_time = round((time.time() - start_time) * 1000, 2)

    return JsonResponse({
        "numbers": result,
        "execution_time_ms": execution_time
    })
