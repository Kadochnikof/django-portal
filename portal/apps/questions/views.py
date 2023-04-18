from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def questions(request):
    return HttpResponse('Скоро здесь будут ответы на частые вопросы')
