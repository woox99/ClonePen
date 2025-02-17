from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    usable_password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Email is optional
        if email == '':
            return email
        elif User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email



