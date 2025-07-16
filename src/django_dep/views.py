from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    """
    A simple view that returns a 'Hello, World!' message.
    """
    return render(request, 'hello_world.html', {'message': 'Hello, World!'})


def healthcheck(request):
    """
    A simple health check view that returns a 200 OK response.
    """
    return HttpResponse("OK", status=200)
