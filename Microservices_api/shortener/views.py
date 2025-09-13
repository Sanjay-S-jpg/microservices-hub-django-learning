import random, string
from django.http import JsonResponse
from .models import ShortURL
from django.views.decorators.csrf import csrf_exempt

# Helper function to generate short code
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# POST /shorten
@csrf_exempt
def shorten_url(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        long_url = data.get("url")

        if not long_url:
            return JsonResponse({"error": "URL is required"}, status=400)

        # Generate unique short code
        code = generate_code()
        while ShortURL.objects.filter(short_code=code).exists():
            code = generate_code()

        short = ShortURL.objects.create(original_url=long_url, short_code=code)
        return JsonResponse({"short_url": f"http://127.0.0.1:8000/expand/{short.short_code}"})

# GET /expand/<shortcode>
def expand_url(request, shortcode):
    try:
        url = ShortURL.objects.get(short_code=shortcode)
        url.visit_count += 1
        url.save()
        return JsonResponse({"original_url": url.original_url})
    except ShortURL.DoesNotExist:
        return JsonResponse({"error": "Shortcode not found"}, status=404)

# GET /stats/<shortcode>
def stats(request, shortcode):
    try:
        url = ShortURL.objects.get(short_code=shortcode)
        return JsonResponse({"short_code": shortcode, "visits": url.visit_count})
    except ShortURL.DoesNotExist:
        return JsonResponse({"error": "Shortcode not found"}, status=404)
