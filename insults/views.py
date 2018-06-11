from django.shortcuts import render

from .insult_generator import generate_insult


def insult(request):
    return render(request, 'insults/insult.html', {'insult': generate_insult()})
