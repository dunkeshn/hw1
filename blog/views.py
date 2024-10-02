from django.http import HttpResponse
from django.shortcuts import render

def page6(request):
    return HttpResponse('Hi, page6!')

def page7(request):
    return HttpResponse('Hi, page7!')

def page8(request):
    return HttpResponse('Hi, page8!')