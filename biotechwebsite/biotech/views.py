from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Students')

def htmlrender(request):
    return render(request, 'template-kush.html')
