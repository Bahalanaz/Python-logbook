from django.http import HttpResponse
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Posts API working", "status": "success"})