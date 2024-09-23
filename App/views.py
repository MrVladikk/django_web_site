from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.db.models import F
from django.contrib.auth import login

# Create your views here.

def index(request):
    latest_q_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_q_list": latest_q_list}
    return render(request, "index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "detail.html", 
            {
                "question": question,
                "error_message": "Вы не выбрали ни одного варианта!", 
            }
        )
    else:
     selected_choice.votes = F("votes") + 1
     selected_choice.save()
    return HttpResponseRedirect(reverse("App:results", args=(question_id, selected_choice.id)))


def results(request, question_id, choice_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = get_object_or_404(Choice, pk=choice_id)
    return render(request, "votes.html", {'question': question, 'choice': choice})