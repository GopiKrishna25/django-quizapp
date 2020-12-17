from django.shortcuts import render
from quizapp.models import Quiz

def quizapp(request):
    results = Quiz.objects.all()
    return render(request,"index.html",{"Quiz":results})
