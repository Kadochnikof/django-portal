from django.shortcuts import render
from .models import Question
from django.http import Http404
# Create your views here.


def questions(request):
    all_questions = Question.objects.order_by('-question_main')
    return render(request, 'questions/list.html', {'questions': all_questions})


def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Exception:
        raise Http404(
            'Ой, кажется, такой страницы нет :(')

    return render(request, 'questions/question.html', {'question': question})
