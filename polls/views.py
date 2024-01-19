from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request,Question,*args, **kwargs):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def  detail(request, question_id):
    return HttpResponse("You are looking at queation %s." %question_id)

def results(request,question_id, *args, **kwargs):
    response = "You are looking at the results of the question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)

def quest(request, *args, **kwargs):
    return render(request, 'index.html', {})

