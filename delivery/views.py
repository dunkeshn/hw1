from django.http import HttpResponse
from django.shortcuts import render

def page3(request):
    return HttpResponse('Hello, page3!')

def page4(request):
    return HttpResponse('Hello, page4')

def page5(request):
    return HttpResponse('Its page5!')