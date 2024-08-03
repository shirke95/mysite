from apps.accounts.forms import RegisterForm
from apps.accounts.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View, generic


# Create your views here.
class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "accounts/profile.html"
    slug_field = "username"


class HomeView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "accounts/home.html"


# def sign_up(request):
#     if request.method == "GET":
#         form = RegisterForm()
#         return render(request, "users/register.html", {"form": form})

#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             messages.success(request, "You have singed up successfully.")
#             login(request, user)
#             return redirect("posts")
#         else:
#             return render(request, "users/register.html", {"form": form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "accounts/register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have singed up successfully.")
            login(request, user)
            return redirect("/accounts/logout")
        else:
            return render(request, "accounts/register.html", {"form": form})
