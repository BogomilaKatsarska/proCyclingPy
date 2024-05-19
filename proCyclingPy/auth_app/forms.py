from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            #TODO: check below
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter your e-mail'
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter your password'
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Enter your password'
        })

        self.fields['role'].label = 'Profile type'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username'})

        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter your password'})


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = UserModel