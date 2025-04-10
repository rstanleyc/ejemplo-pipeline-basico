from django.http import JsonResponse

def ping(request):
    return JsonResponse({'ping': 'ttong'})

def sumar(a, b):
    return a + b
