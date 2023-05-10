from django.shortcuts import render
from .models import Instruction
from django.http import Http404
# Create your views here.

def instructions(request):
    all_instructions = Instruction.objects.order_by('-instruction_name')
    return render(request, 'instructions/list.html', {'instructions' : all_instructions})

def detail(request, instruction_id):
    try:
        instruction = Instruction.objects.get(id = instruction_id)
    except Exception:
        raise Http404('Ой, кажется, такой страницы нет :(')
    
    return render(request, 'instructions/instruction.html', {'instruction': instruction})