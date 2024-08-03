from django.contrib.auth.forms import UserCreationForm

from apps.accounts.models import User


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None

    class Meta:
        model = User
        # fields = "__all__"
        # exclude =
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            "username": None,
            "email": None,
        }
