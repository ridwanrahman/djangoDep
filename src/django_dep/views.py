from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    """
    A simple view that returns a 'Hello, World!' message.
    """
    return render(request, 'hello_world.html', {'message': 'Hello, World!'})

def get_version(request):
    """
    A view that returns the version of the Django application.
    """
    try:
        from importlib.metadata import version
    except ImportError:
        from importlib_metadata import version

    app_version = version("djangoDep")
    # app_version2 = __version__
    return HttpResponse(f"Version: {app_version}", status=200)



def healthcheck(request):
    """
    A simple health check view that returns a 200 OK response.
    """
    return HttpResponse("OK", status=200)
