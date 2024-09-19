from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    """
    content = "<h1>Welcome to my app</h1>"
    return HttpResponse(content)
    """
    return render(request, "home/templates/hello.html",{})