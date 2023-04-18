from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def instructions(request):
    return HttpResponse('Скоро здесь будут инструкции')
