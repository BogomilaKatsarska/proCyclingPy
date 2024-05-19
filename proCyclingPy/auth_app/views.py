from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from proCyclingPy.auth_app.forms import SignUpForm, LoginForm


class SignUpView(CreateView):
    template_name = 'auth_app/signUp.html'
    form_class = SignUpForm
    # success_url = reverse_lazy(index)

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(LoginView):
    template_name = 'auth_app/signIn.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        return self.get_redirect_url()


class SignOutView(LogoutView):
    template_name = 'auth_app/signOut.html'
    next_page = reverse_lazy('index')


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'auth_app/change-password.html'
    # success_url =
