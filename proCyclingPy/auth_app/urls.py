from django.urls import path

from proCyclingPy.auth_app.views import SignUpView, SignInView, SignOutView, ChangePasswordView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='sign up'),
    path('login/', SignInView.as_view(), name='sign in'),
    path('logout/', SignOutView.as_view(), name='sign out'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),
)