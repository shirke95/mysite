from django.urls import path

from apps.polls import views

app_name = "apps.polls"
urlpatterns = [
    path("", views.PollsListView.as_view(), name="polls-list"),
    path("<int:pk>/", views.PollsDetailView.as_view(), name="polls-detail"),
    path("<int:pk>/result/", views.PollsResultsView.as_view(), name="polls-result"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # path("update/", views.PollsUpdateView.as_view(), name="polls-update"),
    path(
        "create/", views.PollsCreateQuestionView.as_view(), name="polls-create-question"
    ),
    path(
        "<int:pk>/create-choice/",
        views.PollsCreateChoiceView.as_view(),
        name="polls-create-choice",
    ),
]
