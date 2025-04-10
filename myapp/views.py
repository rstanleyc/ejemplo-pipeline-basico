from django.http import JsonResponse

def ping(request):
    return JsonResponse({'pingg': 'pong'})

def sumar(a, b):
    return a + b
