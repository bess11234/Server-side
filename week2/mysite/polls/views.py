from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def detail(request, question_id):
    try:
        detail = Question.objects.get(pk=question_id)
        choice = Choice.objects.filter(question_id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, "detail.html", {"question":detail, "choice": choice})

def result(request, question_id):
    return HttpResponse("This is result of question %s" %question_id)

def vote(request, question_id):
    return HttpResponse("This is vote of question %s" %question_id)