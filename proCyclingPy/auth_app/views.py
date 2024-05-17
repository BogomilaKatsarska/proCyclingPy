from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from proCyclingPy.auth_app.forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'auth_app/signUp.html'
    form_class = SignUpForm
    success_url = reverse_lazy(index)

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(LoginView):
    pass


class SignOutView(LogoutView):
    pass


class ChangePasswordView(PasswordChangeView):
    pass
