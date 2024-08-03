from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from apps.accounts.views import ProfileView, RegisterView

app_name = "apps.accounts"

urlpatterns = [
    path(
        "login/", LoginView.as_view(template_name="accounts/login.html"), name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/<slug:pk>/", ProfileView.as_view(), name="profile"),
    # path(
    #     "password_change/done/",
    #     PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path("password_change/", PasswordChangeView.as_view(), name="password_change"),
    # path(
    #     "reset/done/",
    #     PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "password_reset/done/",
    #     PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "password_reset/",
    #     PasswordResetView.as_view(),
    #     name="password_reset",
    # ),
]
