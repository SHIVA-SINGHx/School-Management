from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def school(request):
    return HttpResponse("hello this is school management website")