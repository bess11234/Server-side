from django.shortcuts import render, redirect, get_object_or_404

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
        
        #1
        if (type(choice_id) == int):
            choice = get_object_or_404(Choice, pk=choice_id)
        else:
            raise Exception
        
        #2
        try:
            choice_id = int(choice_id)
            choice = get_object_or_404(Choice, pk=choice_id)
        except Exception:
            raise Exception
        
        choice = Choice.objects.get(pk=choice_id)
        choice.votes += 1
        choice.save()
        return redirect("detail", question_id=question_id)
