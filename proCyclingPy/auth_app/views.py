from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from proCyclingPy.auth_app.forms import SignUpForm, LoginForm
from proCyclingPy.auth_app.signals import create_user_profile


UserModel = get_user_model()

class SignUpView(CreateView):
    template_name = 'auth_app/signUp.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    extra_context = {'title': 'Register'}

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


class ProfileDetailView(DetailView, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        user_type = self.request.user.role
        #TODO: add links to redirects below
        if user_type == 'Cyclist':
            return redirect('details cyclist', pk=self.request.user.pk)
        elif user_type == 'Team Manager':
            return redirect('details team manager', pk=self.request.user.pk)
        else:
            return redirect('select role')


def select_role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role:
            request.user.role = role
            request.user.save()
            create_user_profile(sender=UserModel, instance=request.user, created=True)
            return redirect('details profile')

    return render(request, 'common/select-role.html')


# class CyclistViewForm(forms.ModelForm):
#     model = Cyclist
#
#
# class TeamManagerViewForm(forms.ModelForm):
#     model = TeamManager