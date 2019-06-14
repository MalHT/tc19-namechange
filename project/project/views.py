from django.http import HttpResponse
from django.db import connection

def index(request):
    return HttpResponse("Hello, world")
