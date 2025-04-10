from django.http import JsonResponse

def ping(request):
    return JsonResponse({'ping': 'pong'})

def sumar(a, b):
    return a + b
