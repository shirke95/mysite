from django import forms

from apps.polls.models import Question


class CreateQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = "__all__"
        # fields = ["question_text"]
