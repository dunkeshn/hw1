from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello, world!')

def page1(request):
    return HttpResponse('Hello, page1')

def page2(request):
    return HttpResponse('Its page2!')