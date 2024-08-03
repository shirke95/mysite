from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from apps.polls.forms import CreateQuestionForm
from apps.polls.models import Choice, Question


# Create your views here.
class PollsListView(LoginRequiredMixin, generic.ListView):
    template_name = "polls/question_list.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # """Return the last five published questions."""
        # return Question.objects.order_by("-pub_date")[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class PollsDetailView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = "polls/question_detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class PollsResultsView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = "polls/question_result.html"


@login_required
def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/question_detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse("apps.polls:polls-result", args=(question.id,))
        )


@login_required
def update(request):
    if request.method == "POST":
        form = CreateQuestionForm(request.POST)
    else:
        form = CreateQuestionForm()

    context = {"form": form}
    return render(request, "polls/question_create.html", context)


class PollsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Question
    template_name = "polls/question_update.html"


class PollsCreateQuestionView(LoginRequiredMixin, generic.CreateView):
    model = Question
    fields = "__all__"
    template_name = "polls/question_create.html"

    def get_success_url(self):
        return reverse("apps.polls:polls-list")


class PollsCreateChoiceView(LoginRequiredMixin, generic.CreateView):
    model = Choice
    fields = "__all__"
    template_name = "polls/choice_create.html"

    def get_success_url(self):
        return reverse("apps.polls:polls-list")
