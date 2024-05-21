from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from proCyclingPy.auth_app.models import Profile


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

    def save(self, commit=True):
        user = super().save(commit=commit)
        email = self.cleaned_data['email']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        role = self.cleaned_data['role']
        profile = Profile(
            user=user,
            email=email,
            password1=password1,
            password2=password2,
            role=role,
        )
        if commit:
            profile.save()
        return user


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
        template_name = 'auth'

