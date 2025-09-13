from django.shortcuts import render

from django.http import JsonResponse

# Hardcoded words in the server
WORDS = ["bonfire", "cardio", "case", "character", "bonsai",
         "boolean", "apple", "application", "cat", "dog",
         "dove", "zebra", "zebronics", "bat", "ball",
         "balloon", "banner", "car", "carbon", "carrot"]

def find_unique_prefix(word, words):
    """Find smallest unique prefix for a word among words"""
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        # If this prefix only belongs to one word → it's unique
        matches = [w for w in words if w.startswith(prefix)]
        if len(matches) == 1:
            return prefix
    return word  # fallback (entire word)

def prefixes_view(request):
    keywords = request.GET.get("keywords", "")
    if not keywords:
        return JsonResponse({"error": "keywords param is required"}, status=400)

    keywords_list = keywords.split(",")
    response = []

    for keyword in keywords_list:
        if keyword in WORDS:
            prefix = find_unique_prefix(keyword, WORDS)
            response.append({
                "keyword": keyword,
                "status": "found",
                "prefix": prefix
            })
        else:
            response.append({
                "keyword": keyword,
                "status": "not_found",
                "prefix": "not_applicable"
            })

    return JsonResponse(response, safe=False)

