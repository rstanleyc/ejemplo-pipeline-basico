from django.http import JsonResponse

def ping(request):
    return JsonResponse({'ping': 'tong'})

def sumar(a, b):
    return a + b
