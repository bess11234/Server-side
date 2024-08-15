from django.shortcuts import render, redirect

from django.views import View

from django.http import HttpResponse

from .models import *
# Create your views here.

class IndexView(View):
    def get(self, request):
        lastest_question = Question.objects.order_by("-pub_date")[:5]
        context = {"lastest_question": lastest_question}
        return render(request, "index.html", context)

class DetailView(View):
    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)
        return render(request, "detail.html", {
            "question": question,
            "choices": Choice.objects.filter(question=question).order_by("choice_text")
        })

class VoteView(View):
    def get(self, request, question_id):
        question = Question.objects.get(id=question_id)
        return render(request, "vote.html", {
            "question": question,
            "choices": question.choice_set.all().order_by("choice_text")
        })
        
    def post(self, request, question_id):
        choice_id = request.POST.get("choice") # รับ Argument จาก POST
        choice = Choice.objects.get(pk=choice_id)
        choice.votes += 1
        choice.save()
        return redirect("detail", question_id=question_id)
