from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app2_fun(request):
    return HttpResponse('<h1>This APP2 Function Response</h1>')