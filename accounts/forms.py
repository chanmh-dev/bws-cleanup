from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="Username ( 用户名 )")
    email = forms.EmailField(label="Email ( 电邮 )")
    first_name = forms.CharField(max_length=50, label="Name ( 姓字 )")

    password1 = forms.CharField(
        label="Password ( 密码 )",
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label="Password confirmation( 确认密码 )",
        strip=False,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'password1', 'password2',
                  'email', 'email', ]


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=50, label="Username ( 用户名 )")
    password = forms.CharField(
        label="Password ( 密码 )",
        strip=False,
        widget=forms.PasswordInput,
    )
