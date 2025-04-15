from django.http import JsonResponse

def ping(request):
    #soy yo haciendo un cambio
    return JsonResponse({'ping': 'pong'})

def sumar(a, b):
    return a + b
