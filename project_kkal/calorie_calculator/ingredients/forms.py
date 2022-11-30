from django.contrib.auth.forms import AuthenticationForm as AuthenticationFormGeneric
from django.forms import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from ingredients.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class AuthenticationForm(AuthenticationFormGeneric):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"